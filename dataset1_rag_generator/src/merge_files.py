import glob
import re
import json
import os
from collections import OrderedDict


def parse_md_file(file_path):
    """解析单个MD文件，提取问题数据"""
    file_name = file_path.split('/')[-1].split('.')[0]
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # 使用正则表达式匹配所有问题块
    print(f"exam {file_name} analysising……")
    question_blocks = re.split(r'---+\n', content.strip())
    print(f"There are {len(question_blocks)} questions in {file_name}")
    questions = []
    # 解析每个问题块
    for index, block in enumerate(question_blocks):
        if not block.strip():
            continue
        # 解析问题
        question_match = re.search(r'\*\*(\d+)\.\s*(.*?)\*\*', block)
        if not question_match:
            print(f"current block {index} analysis error, no such format question found")
            continue

        q_id = file_name+"_"+question_match.group(1)
        question_text = question_match.group(2).strip()

        # 解析选项
        options = {}
        option_matches = re.finditer(r'^([A-Z])\)\s*(.*?)$', block, re.MULTILINE)
        for match in option_matches:
            option_key = match.group(1)
            option_text = match.group(2).strip()
            options[option_key] = option_text

        # 解析答案
        answer_match = re.search(r'\*\*Answer:\*\*\s*([A-D])', block)
        answer = answer_match.group(1) if answer_match else None

        if question_text and options and answer:
            questions.append(OrderedDict([
                ("id", q_id),
                ("question", question_text),
                ("options", options),
                ("answer", answer)
            ]))
        else:
            print("there's a none error during (question_text, options, answer), please check the three variables.")
    return questions


def sort_key(question):
    """获取问题的章节编号和子编号，用于后面问题的排序"""
    pattern = re.compile(r'^topic(\d+)_(\d+)$')
    match = pattern.match(question["id"])
    x = int(match.group(1))  # 主编号
    y = int(match.group(2))  # 子编号
    return x, y


def merge_mdfile(file_dir="../output/exams-llm1/", output_file="../output/qa_set/questions—llm1.json"):
    # 配置路径
    file_dir = file_dir  # MD文件所在目录
    output_file = output_file  # 输出JSON文件
    all_questions = []
    # 遍历MD文件，各个解析，将所有问题存入questions字典中
    for file in os.listdir(file_dir):
        questions = parse_md_file(file_dir+file)
        all_questions.extend(questions)

    # 按ID排序字典内容，先按主编号再按子编号从小到大排序
    all_questions.sort(key=lambda item: (sort_key(item)))
    print("完成题目排序主编号、子编号从小到大顺序排列。")

    # 将字典内容保存为JSON文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)

    print(f"成功合并 {len(all_questions)} 个问题到 {output_file}")


def merge_json_files(input_dir, output_file):
    """
    input_dir: 包含JSON文件的目录
    output_file: 合并后的输出文件路径
    """
    merged_data = []
    # 遍历目录下所有.json文件
    for filename in glob.glob(os.path.join(input_dir, "*.json")):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    merged_data.extend(data)  # 合并数组
                else:
                    print(f"警告：{filename} 不是数组格式，已跳过")
        except Exception as e:
            print(f"处理文件 {filename} 时出错：{str(e)}")
    # 写入合并结果
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=2)
    print(f"成功合并 {len(merged_data)} 条数据到 {output_file}")


if __name__ == "__main__":
    # # 读取、解析并合并md文件
    # mdfile_dir = "../output/exams/llm1/"
    # output_file = "../output/qa_set/questions-llm.json"
    # merge_mdfile(mdfile_dir, output_file)

    # 读取合并json文件
    json_dir = "../output/qa_set/"
    out_file = "../output/all_questions.json"
    merge_json_files(json_dir, out_file)

