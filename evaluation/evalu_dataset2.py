import datetime
import json
import os
import re
import time
from pathlib import Path
import yaml
from langchain_openai import ChatOpenAI


# 1.从文件中读取试题序列
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
    print(questions[0])
    return questions


# 2.调用大模型对置错文件进行分析
def get_model_answer(question, llm):
    """
    调用大模型对单个问题作答
    :param question: 单个问题
    :return: 大模型作答结果，只返回一个结果
    """
    prompt = f"""
            Based on your knowledge of the theory and practice of automated formal analysis of cryptographic protocol security, 
            analyze the following formal model file delimited by "'''" to determine whether there are any errors. 
            Please provide a boolean answer (True or False) without any explanation. If there are errors, return True; if there are no errors, return False.:
            '''{question}'''
            """

    try:
        answer = llm.invoke(prompt).content

        if answer in ["True", "False"]:
            print(f"✅ 模型返回有效答案：{answer}")
            return answer
        else:
            print(f"⚠️ 模型返回无效答案：{answer}")
            return answer  # 表示无效答案
    except Exception as e:
        print(f"❌ 调用模型失败：{e}\n 重新再调用一遍")
        return 0  # 表示错误


# 3.全部问题作答与结果存储
def evaluate_dataset(all_formals, llmpara_file):
    """
    调用大模型对全部问题进行作答，并将结果和相关的重要信息存储到文件中
    :param all_formals:是一个列表，这里我们只获取文件的路径列表，json文件中读取的包含数据集2各种参数的列表，其中包括置错形式化文件的地址。
    :param llmpara_file:调用的各个大模型的参数信息
    :return:返回字典型的结果
    """

    combined_data = []
    results_llms = []  # 用一个列表表示所有大模型做题的结果信息，列表每一项的内容是一个results列表。
    print(llmpara_file)
    with open(llmpara_file, "r", encoding="utf-8") as f:
        llmparameter_list = json.load(f)
    print(llmparameter_list[0])
    for item in llmparameter_list:
        print(f"📊正在使用大模型{item['refer_model_name']}对该数据集做测试评估")
        llm = ChatOpenAI(model_name=item["refer_model_name"], openai_api_base=item["refer_api_base"],
                         openai_api_key=item["refer_api_key"])
        start_time = time.time()
        results = []  # 用一个列表存储某个大模型产生的结果，列表内容包括针对各题做的结果，和总结果。
        for i, single_formal in enumerate(all_formals):
            sigle_start_time = time.time()
            file_path = single_formal["dst_path"] # 这个路径是创建的时候在dataset2_generator这个文件夹中它们的相对路径，在评估文件夹中使用还进行修改才能读取到该文件。
            file_path = file_path.replace("../output/with_err_files", "../dataset2_generator/output/with_err_files")
            with open(file_path, "r", encoding='utf-8') as f:
                formal_content = f.read()
            print(f"🔄 正在处理第{i + 1}个数据文件：{file_path}")
            is_result = 0
            while not(is_result): # 针对由于网络或调用次数限制导致的调用模型失败处理
                llm_result = get_model_answer(formal_content, llm)
                is_result = llm_result
            correct_answer = single_formal["has_err"]
            single_end_time = time.time()
            results.append({
                "id": i,
                "err_file": single_formal["dst_path"],
                "correct_answer": correct_answer,
                "model_answer": llm_result,
                "single_time_span": single_end_time - sigle_start_time,
                "is_result_correct": llm_result == correct_answer
            })
            print(f"✅ 处理第{i + 1}个数据文件完成，用时:{single_end_time - sigle_start_time}秒")
            # time.sleep(3)  # 防止调用频率过高，导致部分闭源的在线大模型被禁止访问
        end_time = time.time()
        time_span = end_time - start_time
        correct_num = sum(1 for result in results if result["is_result_correct"])
        summary_data = {
            "llm_name": item["refer_model_name"],
            "start_time": start_time,
            "end_time": end_time,
            "time_span": time_span,
        }
        combined_data = results + [summary_data]
        print(f"\n🔄 分析总数：{len(results)}")
        print(f"✅ 总用时：{time_span}")
        print(f"🎯 分析正确率：{correct_num/len(results):.2f}")
        print("💎将详细结果存至指定文件......................................\n\n")
        results_llms.append(combined_data)  # combined_data是一个大模型对数据集中所有文件执行的结果，results_llms相当于是所有大模型的执行结果。
    return results_llms


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


def run(formal_file_dir="../dataset2_generator/output/test_set/",
        llms_para="../dataset1_rag_generator/config/refer_llms.json",
        result_directory="./results/dataset2/",
        prefix_filename="haserr_judge_", extension="json"):
    """
    调用评估函数，并将评估结果存到指定目录下
    :param llms_para: 读入，将要使用的大模型参数列表
    :param formal_file_dir: 读入，形式化文件数据集参数的存储目录
    :param result_directory: 输出，文件存储的目录
    :param prefix_filename: 输出，文件命名添加的区别性前缀
    :param extension: 输出，文件的存储格式
    :return: null
    """
    formal_file_para = json_files_loader(formal_file_dir)  # 读取目录下的所有json文件，只有一个文件时也可以
    all_llms_results = evaluate_dataset(formal_file_para, llms_para)  # 使用llms_para中不同的大模型对formal_file_para中的各个文件进行评估
    # 评判完毕后将结果存储到指定文件中，文件目录是result_directory，文件命名为判定类型+大模型名称
    for index, one_llm_result in enumerate(all_llms_results):
        print(f"🔄 正在存储第{index + 1}个大模型的结果")
        try:
            write2file(content=one_llm_result,
                       path_dir=result_directory,
                       file_name=prefix_filename + one_llm_result[-1]["llm_name"],
                       file_type=extension)
        except Exception as e:
            print(f"存储txt文件发生错误：{e}")


if __name__ == "__main__":
    # # 使用测试文件和测试大模型，测试总体过程。
    # run(formal_file_dir="../dataset2_generator/output/test_set/",
    #     llms_para="../dataset1_rag_generator/config/test_llms.json",
    #     result_directory="./results/dataset2/",
    #     prefix_filename="haserr_judge_", extension="json")

    # 使用实际文件和实际测评模型，运行总体过程
    run(formal_file_dir="../dataset2_generator/output/dataset_remote/",
        llms_para="../dataset1_rag_generator/config/test_llms.json",
        result_directory="./results/dataset2/",
        prefix_filename="haserr_judge_", extension="json")
