import datetime
import glob
import json
import os

from base_src.llms import formal_deepseekv3_ali


def clean(formal_sen):
    # 去除输入字符串的首尾特殊字符，判断首字符是否为字母，是字母则返回字符串，否则返回空
    dst = formal_sen.strip()
    if dst:
        if dst[0].isalpha():
            return dst
    return ""


def nl_dsc_gen(dst):
    prompt = f"""There is a sentence written in formal language used by proverif, the sentence is surrounded by <>: <{dst}>. as an expert major in protocol formal verification, please translate the sentence into nature language."""
    result = formal_deepseekv3_ali.execute_prompt(prompt)
    return result


def generate_json(source_file, output_json):
    """
    :param source_file: 输入文件路径（每行仅含目标形式化语言内容）
    :param output_json: 输出JSON文件路径
    """
    result = []
    with open(source_file, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f, 1):
            print(f"开始第{idx}条数据的逆向翻译处理过程")
            dst = clean(line)  # 清洗逐行读取的数据
            if not dst:
                print("——此行数据不是形式化内容，本过程不处理")
                continue  # 跳过空行、路过注释行，判定过程在clean函数中执行
            try:
                # 基于大模型自动生成source内容
                source = nl_dsc_gen(dst)
                print("——这是未经过大模型修改前的逆向翻译内容：" + source)
                # 我们先将不满足逆向翻译结果的条件设置成生成内容大于1行，因为如果多于1行，大概率是说了其它解释信息
                if len(source.splitlines()) > 1:
                    modify_prompt = source + "\n\n" + "The content you generated above contains too much redundant information. Remove this redundancy so that the output only includes a natural language description of the formalized content."
                    source = formal_deepseekv3_ali.execute_prompt(modify_prompt)
                    print("——这是经过大模型一次修改后的逆向翻译内容：" + source)
                # 一次修改后将改后内容存入文件
                result.append({
                    "instruct": "translate the following nature language text into formal language used by proverif",
                    "input": source,
                    "output": dst
                })
            except Exception as e:
                # Generate timestamp for unique backup filename
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_file = output_json.replace('.json', f'_backup_{timestamp}_at_line_{idx}.json')

                # Save existing results with metadata
                with open(backup_file, 'w', encoding='utf-8') as backup_f:
                    backup_data = {
                        "metadata": {
                            "last_successful_idx": idx - 1,
                            "error_line": idx,
                            "error_time": timestamp,
                            "error_content": str(e)
                        },
                        "results": result
                    }
                    json.dump(backup_data, backup_f, ensure_ascii=False, indent=2)
                print(f"Error occurred at line {idx}. Backup saved to {backup_file}")
                raise  # Re-raise the exception after saving backup
            print(f"**************************完成第{idx}行语句生成，进入下一个语句生成过程*********************************")
            # break
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"。。。。。。。。。。。。。。。。。。。。生成完成！共处理 {len(result)} 条数据。。。。。。。。。。。。。。。。。。。。")


def generator_batch(source_path, output_path):
    directory = source_path
    for filename in os.listdir(directory):
        print(f"开始处理{directory}目录下的第一个文件:{filename}")
        if filename.endswith(".txt"):
            source_txt = os.path.join(directory, filename)
            output_json = os.path.join(output_path + os.path.splitext(filename)[0] + '.json')
            generate_json(source_txt, output_json)
        print("完成第一个文件的逆向形式化翻译")
        # break


def generator_single(source_file, output_file):
    generate_json(source_file, output_file)


def merge_json_files(input_dir, output_file):
    """
    合并目录中所有JSON数组文件
    参数：
    input_dir: 包含JSON文件的目录路径
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


# 使用示例
if __name__ == "__main__":
    # # 批量处理source_path目录下所有文件
    # source_path = "./dataset4/apic/"
    # output_path = "./dataset4/middle_dataset3/"
    # generator_batch(source_path, output_path)

    # # 单个文件处理
    # source_file = "./dataset4/apic/UAF.txt"
    # output_file = "./dataset4/middle_dataset3/UAF.json"
    # generator_single(source_file, output_file)

    # 多个json合成一个
    merge_json_files("../../middle_results/middle_dataset3/", "dataset4/dataset3_paral_senten.json")
