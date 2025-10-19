import json
from tqdm import tqdm
from langchain_openai import ChatOpenAI
import time
from pathlib import Path
import yaml
import datetime
import os

def answer_format(res_str):
    return res_str


def response_compare(response, benchmark):
    # 判断是否一个完整的形式化表达式
    if response == benchmark:
        # 如果是完整表达式再进行下一步判断内容的相似程度，返回一个相似值，完全相同为1
        return 1
    # 如果不是完整形式化表达式，则返回0
    else:
        return 0    

# 1.加载准备使用大模型处理的数据集
def json_files_loader(input_dir=""):
    """
    加载数据集，这个函数可以直接加载一个文件夹下的全部json，就不用前面那个合并的操作了。
    :param input_dir: 输入文件所在目录
    :return: 返回问题列表，
    """
    questions = []
    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(input_dir, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                questions.extend(data)
    print(f"✅ 成功加载 {len(questions)} 条数据")
    return questions


# 2.调用大模型对置错文件进行分析
def get_model_answer(instance, llm):
    """
    调用大模型对单个问题作答
    :param instance: json数据集文中的单个实例
    :llm: 分析当前实例使用的大模型
    :return: 大模型作答结果，只返回一个结果
    """
    instruction = instance['instruct']
    nl_input = instance['input']
    prompt = instruction + nl_input + "the result you output should not include redundant information only reserve the formal expressions"
    try:
        answer = llm.invoke(prompt).content
        if answer in ["True", "False"]:
            print(f"✅ 模型返回有效答案：{answer}")
            return answer
        else:
            print(f"⚠️ 模型返回无效答案：{answer}")
            return f"⚠️ 模型返回无效答案：{answer}"  # 表示无效答案
    except Exception as e:
        print(f"❌ 调用模型失败：{e}")
        return f"❌ 调用模型失败：{e}"  # 表示错误


# 3.全部大模型对全部数据集翻译结果及存储
def evaluate(data_list, llmpara_list):
    """
    调用本地模型，完成翻译，然后比对结果
    """
    all_llm_results=[]
    for llmpara in llmpara_list:
        one_llm_result = []
        print(f"📊  开始测试大模型{llmpara["refer_model_name"]}在数据集3上的翻译能力")
        start_time = time.time()
        llm_inst = ChatOpenAI(model_name=llmpara["refer_model_name"], openai_api_base=llmpara["refer_api_base"], openai_api_key=llmpara["refer_api_key"])
        for index, instance in enumerate(data_list):
            correct = 0
            total = 0
            print(f"🔄  进入实例{index}: {instance}翻译能力测试")
            single_start_time = time.time()
            retry = True
            while retry:
                response = get_model_answer(instance, llm_inst)
                print(f"针对\'{instance}\'\n大模型给出的形式化翻译是：" + response)
                # 判断返回结果是否符合选项格式要求，这个返回结果应当只有一行，且这一行也只有形式化表达式
                formated_response = answer_format(response)
                # 如果返回的内容是想要的答案样式，就将retry置否，这能使程序跳出while循环进入下一个问题的处理。
                if formated_response:
                    print("此答案格式符合预期，计算内容相似度")
                    compa_result = response_compare(formated_response, instance['output'])
                    correct += compa_result
                    total += 1
                    retry = False
                # 如果返回的答案不符合格式要求，修改prompt，再让大模型处理一遍这个结果
                else:
                    print("此答案不格式不符合预期格式，修改prompt重新再处理一遍当前question")
                    prompt = prompt + "\n\n" + response + "the response is not a specification only use the proverif model language"
            single_end_time = time.time()
            single_time_span = single_end_time-single_start_time
            one_llm_result.append({
                "instance_num": index,
                "raw_nl_spec": instance["input"],
                "llm_resp": response,
                "prcesed_resp": formated_response,
                "is_correct": compa_result,
                "accuracy": correct/total,
                "single_time_span": single_time_span
            })
        end_time = time.time()
        all_time_span = end_time-start_time
        summary_data = {
            "llm_name": llmpara["refer_model_name"],
            "start_time": start_time,
            "end_time": end_time,
            "time_span": all_time_span,
        }
        combined_data = one_llm_result + [summary_data]
        all_llm_results.append(combined_data)
        print(f"\n🔄 分析总数：{len(one_llm_result)}")
        print(f"✅ 总用时：{all_time_span}")
        print("相似度总和为：" + str(correct) + "\n参与评估实例数为：" + str(total))
        print("💎将详细结果存至指定文件......................................\n\n")
    return all_llm_results


def write2file(content, path_dir="", file_name="", file_type=""):
    results_dir = path_dir
    Path(results_dir).mkdir(parents=True, exist_ok=True)
    results_name = file_name
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if file_type == "json":
        with open(f"{results_dir}/{results_name}.{file_type}", "w", encoding="utf-8") as f:
            f.write(f"// 写入时间: {timestamp}\n\n")
            f.write(json.dumps(content, ensure_ascii=False, indent=4))
    elif file_type == "txt":
        with open(f"{results_dir}/{results_name}.{file_type}", "w", encoding="utf-8") as f:
            f.write(f"[{timestamp}]\n\n{content}")
    elif file_type == "yaml":
        with open(f"{results_dir}/{results_name}.{file_type}", "w", encoding="utf-8") as f:
            f.write(f"// 写入时间: {timestamp}\n\n")
            yaml.dump(content, f, allow_unicode=True)


def run(dataset_dir, llm_path, result_directory, prefix_filename, extension):
    # 读取数据集列表
    data_list = json_files_loader(dataset_dir)
    # 读取大列表
    with open(llm_path, "r", encoding="utf-8") as f:
        llmparameter_list = json.load(f)
    # 开始用不同大模型对数据集列表中的数据进行评估
    allm_results = evaluate(data_list, llmparameter_list)
    # 存储数据
    for one_llm_result in allm_results:
        try:
            write2file(content=one_llm_result,
                       path_dir=result_directory,
                       file_name=prefix_filename + one_llm_result[-1]["llm_name"],
                       file_type=extension)
        except Exception as e:
            print(f"存储txt文件发生错误：{e}")


if __name__ == "__main__":
    run(dataset_dir="./dataset3_reverse_generator/test_set/",
        llm_path="./dataset1_rag_generator/config/test_llms.json",
        result_directory="./results/dataset3/",
        prefix_filename="translate_", extension="json")
    # print(type(response_compare("abc","123")))
