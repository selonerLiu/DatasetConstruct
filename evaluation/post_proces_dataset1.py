import datetime
import json
import os
import re
import time
from pathlib import Path
import yaml

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

def post_process_opera(raw_text):
    """
    根据大模型反馈的结果特点，提取出只有答案字母的结果。只负责提取一段文本中的答案
    :param raw_text:
    :return:
    """
    # 预处理：移除<think>标签及其内容
    clean_text = re.sub(r'<think>.*?</think>', '', raw_text, flags=re.DOTALL)

    # 获取最后3行内容（答案通常出现在最后几行）
    lines = clean_text.strip().splitlines()
    search_text = '\n'.join(lines[-3:]) if len(lines) > 3 else clean_text

    # 按优先级尝试多种匹配模式
    patterns = [
        r'\\boxed{([A-D])}',  # 处理 \boxed{B} 格式
        r'(?:Answer|Correct Answer|Final Correct Answer)[\s\*:]*\**([A-D])\**',  # 处理Answer: A格式
        r'The correct answer is\**\s*([A-D])\**',  # 处理"correct answer is C"格式
        r'So, the letter is ([A-D])\.',  # 处理"So, the letter is B"格式
        r'^\s*([A-D])[\s\*\.]*$',  # 处理单独一行字母格式
        r'[^A-Da-d]([A-D])[\s\*\.]*$'  # 处理行尾字母格式
    ]

    for pattern in patterns:
        match = re.search(pattern, search_text, re.IGNORECASE)
        if match:
            return match.group(1).upper()

    # 终极方案：查找最后一个出现的大写字母(A-D)
    last_letter_match = re.findall(r'([A-D])', search_text)
    if last_letter_match:
        return last_letter_match[-1]
    return None  # 未找到答案

def post_process_dataset(extracted_file_path):
    """
    调用post_process_opera处理文本，然后重新评估去除后内容是否正确，计算相关参数，修改json文件中最后一条数据，增加修改后的相应参数值。
    :extracted_file_path:待处理文件的路径。新生成文件与待处理文件在同一路径下，名称后加一个"_extr"后缀。
    :return: 修改后的数据正确率，将修改后的数据重新存储到新文件中。
    """
    # 读取json格式文件
    # 我们在生成json文件的时候第一行插入了时间信息，这里需要路过第一行再读才能读出正确的json文件形式
    skip_lines = 1  # 没有在第一行添加额外信息的要把跳过的行数设置为0。
    with open(extracted_file_path, "r", encoding="utf-8") as f:
        for _ in range(skip_lines):
            next(f)  # 读取并丢弃一行
        # 读取剩余内容
        content = f.read()
        try:
            data = json.loads(content)
        except json.JSONDecodeError as e:
            print(f"JSON解析错误: {e}")
    # 循环读取除最后一条数据之外每一条数据的"model_answer"键对应的值，每个值使用post_process_opera函数处理一遍
    count = 0
    for item in data[:-1]:
        item["model_answer_ext"] = post_process_opera(item["model_answer"])
        # 对比该条数据新的"model_answer"和"correct_answer"键对应的值，并根据对比结果更正"is_correct"键对应的值
        if item["model_answer_ext"] == item["correct_answer"]:
            item["is_correct_ext"] = True
        else:
            item["is_correct_ext"] = False
    # 修正完所有数据后，再次读取data的每条数据判断"is_correct"为True的条目数，修改最后一条数据的"correct_count"和"accuracy"值
    for item in data[:-1]:
        if item["is_correct_ext"]:
            count += 1
    data[-1]["correct_count_ext"] = count
    data[-1]["accuracy_ext"] = count / (len(data) - 1) * 100
    # 将修改后的数据重新存储到新文件中
    out_file_path = "./results/dataset1/"
    filename = os.path.splitext(os.path.basename(extracted_file_path))[0]
    write2file(content=data, path_dir=out_file_path, file_name=f"{filename}_extr", file_type="json")
    print(f"完成修正后的文件存储，已经存储到{out_file_path}{filename}_extr.json文件下")

if __name__== "__main__":
    # # 测试从回复中提取答案的方法正确性
    # test_cases = 
    #     ["<think>...</think>\n\nC",
    #     "<think>...</think>\n\n**Answer: A**",
    #     "<think>...</think>\n\nAnswer: B",
    #     "<think>...</think>\n\nAnswer: **A**",
    #     "<think>...</think>\n\nAnswer: B",
    #     "<think>...</think>\n\nAnswer:\nB",
    #     "<think>...</think>\n\n*Final Correct Answer: B*",
    #     "<think>...</think>\n\n**Answer:** \\boxed{B}",
    #     "<think>...</think>\n\n**Answer:** \n\\boxed{B}",
    #     "<think>...</think>\n\nThe correct answer is **C**.",
    #     "<think>...</think>\n\nThe correct answer is C....",
    #     "<think>...</think>\n\nwEfDewC. ...",
    #     "<think>...</think>\n\nThe correct answer is:\n\n**B: .wefwefjolijwfi.",
    #     "<think>...</think>\n\nSo, the letter is B.",
    #     "<think>...</think>\n\nSo, the answer is D.",
    #     "C"]
    # for i, text in enumerate(test_cases):
    #     print(f"Case {i + 1}: {post_process_results(text)}")

    # 正式运行，直接针对某一大模型的输出结果进行处理。
    post_process_dataset("./results/dataset1/eval_results_llm_local_dsr14b.json")
    # # 正式运行，使用evaluate_extracted_data重新评估几个推理大模型的能力指标。或者对某一目录下所有大模输出结果逐个处理。
    # directory = "./results/dataset1/"
    # for filename in os.listdir(directory):
    #     if filename.endswith('.json'):
    #         file_path = os.path.join(directory, filename)
    #         print(file_path)
    #         try:
    #             evaluate_extracted_data(file_path)
    #         except Exception as e:
    #             print(f"Error reading {filename}: {e}")
