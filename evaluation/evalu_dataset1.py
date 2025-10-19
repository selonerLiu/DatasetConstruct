import datetime
import json
import os
import re
import time
from pathlib import Path
import yaml
from langchain_openai import ChatOpenAI


# 1.从文件中读取试题序列
def load_questions(input_dir=""):
    """
    加载数据集，这个函数可以直接加载一个文件夹下的全部json，就不用前面那个合并的操作了。
    :param input_dir: 输入文件夹
    :return: 返回问题列表
    """
    questions = []
    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(input_dir, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                questions.extend(data)
    print(f"✅ 成功加载 {len(questions)} 道题目")
    print(questions[0])
    return questions


# 2.调用大模型对单个问题作答
def get_model_answer(question, llm):
    """
    调用大模型对单个问题作答
    :param question: 单个问题
    :return: 大模型作答结果，只返回一个结果
    """
    prompt = f"""
            Please select the correct answer based on the following question and options (return only the letter of the option A-D, no explanation):
            question：{question["question"]}
            options：
            A. {question["options"]['A']}
            B. {question["options"]['B']}
            C. {question["options"]['C']}
            D. {question["options"]['D']}
            """

    try:

        answer = llm.invoke(prompt).content

        if answer in ["A", "B", "C", "D", "a", "b", "c", "d"]:
            print(f"✅ 模型返回有效答案：{answer}")
            return answer
        else:
            print(f"⚠️ 模型返回无效答案：{answer}")  # 表示无效答案
            return answer
    except Exception as e:
        print(f"❌ 调用模型失败：{e}")
        return f"❌ 调用模型失败：{e}"  # 表示错误


# 3.全部问题作答与结果存储
def evaluate_dataset(all_questions, llmpara_file):
    """
    调用大模型对全部问题进行作答，并将结果和相关的重要信息存储到文件中
    :param all_questions:数据集的所有题目
    :param llmpara_file:调用的各个大模型的参数信息
    :return:返回字典型的结果
    """

    results_llms = []  # 用一个列表表示所有大模型做题的结果信息，列表每一项的内容是一个results列表。

    with open(llmpara_file, "r", encoding="utf-8") as f:
        llmparameter_list = json.load(f)
    for item in llmparameter_list:
        print(f"📊正在使用大模型{item['refer_model_name']}对该数据集做测试评估")
        llm_num = item["num"]
        llm = ChatOpenAI(model_name=item["refer_model_name"], openai_api_base=item["refer_api_base"],
                         openai_api_key=item["refer_api_key"])
        start_time = time.time()
        results = []  # 用一个列表存储某个大模型产生的结果，列表内容包括针对各题做的结果，和总结结果。
        i = 0
        for i, single_question in enumerate(all_questions):
            # if i<=1004: # 针对有时执行出错的情况，从某一个序号往后再继续执行。
            #     continue
            # else:
            print(f"🔄 正在处理第 {i + 1} 题：{single_question['id']}")
            llm_result = get_model_answer(single_question, llm)
            correct_answer = single_question["answer"]
            results.append({
                "id": i,
                "topic": single_question["id"],
                "question": single_question["question"],
                "correct_answer": single_question["answer"],
                "model_answer": llm_result,
                "is_correct": llm_result == correct_answer
            })
            # time.sleep(20)
        end_time = time.time()
        time_span = end_time - start_time
        correct_count = sum(1 for r in results if r["is_correct"])
        total = len(results)
        accuracy = correct_count / total * 100 if total > 0 else 0
        summary_data = {
            "start_time": start_time,
            "end_time": end_time,
            "time_span": time_span,
            "model_name": llm_num,
            "correct_count": correct_count,
            "total": total,
            "accuracy": accuracy,
            "llm_num": llm_num
        }
        combined_data = results + [summary_data]
        print(f"\n🔄 总答题数：{total}")
        print(f"✅ 正确数：{correct_count}")
        print(f"🎯 正确率：{accuracy:.2f}%")
        print("💎将详细结果存至指定文件......................................\n\n")
        write2file(content=combined_data, path_dir="./results/dataset1/",
                   file_name="eval_results_" + combined_data[-1]["llm_num"], file_type="json")
    results_llms.append(combined_data)
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


def run(questions_dir="../dataset1_rag_generator/output/test_set/", directory="./results/dataset1/",
        prefix_filename="eval_results_", extension="json"):
    """
    综合各函数，获取最终结果，将结果存到文件中
    """
    questions = load_questions(questions_dir)
    eval_results = evaluate_dataset(questions, "../dataset1_rag_generator/config/refer_llms.json")
    for item in eval_results:
        try:
            write2file(content=item, path_dir=str(directory), file_name=prefix_filename + item[-1]["llm_num"],
                       file_type=extension)
        except Exception as e:
            print(f"存储txt文件发生错误：{e}")

if __name__ == "__main__":
    # # 试试效果，用一个大模型测试当前数据在当前模型下的运行情况
    # questions = load_questions("../dataset1_rag_generator/output/test_set/")
    # # 调用evaluate_dataset函数，将结果存到指定文件中，指定的文件直接调用write2file在函数体中写死了。
    # results = evaluate_dataset(questions, "../dataset1_rag_generator/config/refer_llms.json")
    
    # 正式运行，在问答数据集中评估各大模型的正确率
    questions = load_questions("../dataset1_rag_generator/output/qa_set/")
    results = evaluate_dataset(questions, "../dataset1_rag_generator/config/refer_llms.json")




# def llm_answer_compare(response, benchmark):
#     """
#     用于评判大模型输出结果正确与否，主要针对大模型有时候输出的是正确的但是对比方法可能会导致不正确的情况
#     :param response: 大模型的直接输出
#     :param benchmark: 数据集中的标准答案
#     :return:True 或 False
#     """
#     stred_benchmark = ""
#     if isinstance(benchmark, list):
#         stred_benchmark = "".join(benchmark)
#         stred_benchmark = stred_benchmark.lower()
#     elif isinstance(benchmark, str):
#         stred_benchmark = benchmark.lower()
#
#     if sorted(stred_benchmark) == sorted(response):
#         return True
#     else:
#         return False


# def recycle4wrong_results():
#     """
#     处理大模型返回结果不符合预期的情况，对于一些本身答案正确但是多了一些冗余表达致使程序将其判断为误的情况，重新调用大模型直到返回正确格式的数据。
#     :return:
#     """
#         retry = True
#         while retry:
#             response = evaluate_llm.execute_prompt(prompt)
#             print(f"针对\'{question}\'问题给出的答案是：\n" + response)
#             # 判断返回结果是否符合选项格式要求，并将其处理成一个纯字符串（答案可以是错的，但格式一定要是对的）
#             formated_response = format_llm_response(response)
#             # 如果返回的内容是想要的答案样式即ABCD中的一个字母，就将retry置否，这能使程序跳出while循环进入下一个问题的处理。
#             if formated_response:
#                 print("此答案格式符合预期，进入下一个question的处理")
#                 if llm_answer_compare(formated_response, item['answer']):
#                     correct += 1
#                 else:
#                     print("此题大模型给出的答案不正确")
#                 total += 1
#                 retry = False
#             # 如果返回的答案不是指定选项，修改prompt，再让大模型处理一遍这个结果，直到输出的是一个字母为止
#             else:
#                 print("此答案不格式不符合预期格式，修改prompt重新再处理一遍当前question")
#                 prompt = prompt + "\n\n" + response + "the response is not a character represent one of the options, modify the result to be a character"
