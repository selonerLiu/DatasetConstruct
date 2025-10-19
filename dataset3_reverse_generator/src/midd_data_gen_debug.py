import json
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
            dst = clean(line)  # 清洗逐行读取的数据
            if not dst:
                continue  # 跳过空行，直接进入下一个循环，continue后面的内容不再执行
            # 调试：每输出一个内容先暂停，用户确认，清洗后的内容是否符合标准，符合之后再进入下一个循环
            print("读取的内容是：" + dst)
            while True:
                user_input = input("核对清洗后的内容，核对无误按回车继续，输入 'esc' 退出循环: ")
                if user_input == "":
                    break
                elif user_input == "esc":
                    break
            if user_input.lower() == "esc":
                print("停止下一条数据的读取操作")
                result.append({
                    "instruct": "translate the following nature language text into formal language used by proverif",
                    "input": source,
                    "output": dst
                })
                break  # 输入 exit 则提前终止循环

            # 基于大模型自动生成source内容
            source = nl_dsc_gen(dst)
            print(source)
            # 调试：每输出一个内容先暂停，等待用户确认后再进行下一个循环，用户输入任何字符都作为prompt连接到上一步大模型的输出上，再一起输入给大模型重新输出。
            while True:
                user_input = input("核对翻译后的内容:1.内容符合要求按回车继续下一条；2.内容不符合，输入对大模型生成内容的修改建议；3.输入esc结束任务只将当前读取翻译内容存入文件：")
                if user_input == "":
                    break
                elif user_input == "esc":
                    print("停止下一条数据的翻译操作")
                    result.append({
                        "instruct": "translate the following nature language text into formal language used by proverif",
                        "input": source,
                        "output": dst
                    })
                    break
                else:
                    modify_prompt = source + "\n\n" + user_input
                    source = formal_deepseekv3_ali.execute_prompt(modify_prompt)
                    print(source)
                    continue
            print("结束当前人在循环的形式化语句反译过程")
            result.append({
                "instruct": "translate the following nature language text into formal language used by proverif",
                "input": source,
                "output": dst
            })
            if user_input == "esc":
                print("停止下一条数据的读取与翻译操作，结束循环")
                break
            print("**************************进入下一个语句的循环生成过程*********************************")
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"生成完成！共处理 {len(result)} 条数据")


# 使用示例
if __name__ == "__main__":
    generate_json(source_file="../../dataset4/apic/UAF.txt", output_json="./dataset4/bilin_sen.json")

    # source = nl_dsc_gen("set displayDerivation = false")
    # print(source)
