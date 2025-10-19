import json
from tqdm import tqdm
from base_src import llms


#  % 1.读json文件，返回源和标准文件的地址 %
def read_json(json_path):
    """
    从json文件中读取源和标准内容
    :param json_path:数据集json文件的路径
    :return:待分析文件列表，以及标准结果列表。
    """
    source_file_list = []
    benchmark_file_list = []
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON file: {e}") from e
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {e}") from e
    except Exception as e:
        raise RuntimeError(f"An error occurred: {e}") from e
    for single_protocol in tqdm(data):
        source_file_list.append(single_protocol["source style"])
        benchmark_file_list.append(single_protocol["destin style"])
        if not isinstance(single_protocol["source style"], str) or not isinstance(single_protocol["source style"], str):
            raise KeyError("JSON 中必须包含 'source style' 和 'destin style' 两个字符串类型的键")
    return source_file_list, benchmark_file_list


#  % 2.读取源文件，返回源文件中的内容 %
def read_source_file(source_file):
    """
    从源文件中读取内容
    :param source_file:源文件名
    :return:源文件内容
    """
    source_file_path = "./dataset4/anb/" + source_file
    with open(source_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content


#  % 3.基于源文件内容组合prompt，调用大模型，返回大模型生成结果 %
def get_model_answer(source_content, llm):
    """
    以sourcefile内容构造完整的输入prompt，调用大模型对sourcefile进行处理，并返回处理结果
    :param source_content:读取源文件获取的流数据内容
    :return:大模型针对源文件的处理结果。
    """
    task = "Above is the AnB description of cryptographic protocol, your task is to translate it into formal description, the formal description should be in consistent with the proverif input format"
    prompt = source_content + "\n'n" + task
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
    return generate_result


#  % 4.读取标准文件，返回标准文件中的内容 %
def read_benchmark_file(benchmark_file):
    """
    从标准文件中读取内容
    :param benchmark_file:标准文件名称
    :return: 标准文件内容
    """
    benchmark_file_path = "./dataset4/apic/" + benchmark_file
    with open(benchmark_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content


#  % 5.对比大模型生成结果和标准文件内容，评判结果正确性 %
def compare(model_result, benchmark_content, llm):
    """
    对比大模型生成结果和标准文件内容，评判结果正确性
    :param model_result: 大模型生成结果
    :param benchmark_content: 标准结果
    :return: 正确性指标值
    """
    # 直接调用大模型让其给出一个两者一致性的评分
    evalu_prompt = "please evaluate the consistence of the above two formal specifications of a same protocol from two aspect: 1.. finally give a number range in (1,10) to represent the similarity\n"
    specification1 = model_result
    specification2 = benchmark_content
    evalu_prompt = "specification 1:\n" + specification1 + "\n" + "specification 2:\n" + specification2 + "\n" + evalu_prompt
    result = llm.execute_prompt(evalu_prompt)

    return result


def evalu_main(jsonpath):
    """
    完成评估工作
    :return: 存储数据到文件、绘图等
    """
    s_list, d_list = read_json(jsonpath)
    evalu_result_list = []
    for i in range(len(s_list)):
        print(i)
        s_content = read_source_file(s_list[i])
        gen_result = get_model_answer(s_content, llms.llm_for_gen)
        d_content = read_benchmark_file(d_list[i])
        evalu_result = compare(gen_result, d_content, llms.llm_for_gen)
        evalu_result_list.append(evalu_result)
    return evalu_result_list



if __name__ == "__main__":
    # # % 测试从json中读取文件列表，并根据文件名列表读取文件内容
    # s_list, d_list = read_json("./dataset4/dataset4_para_protoc.json")
    # s_content = read_source_file(s_list[0])
    # d_content = read_benchmark_file(d_list[0])
    # print(s_content)
    # print("****************************generative results as follows********************************")
    # # print(d_content)

    # # % 测试调用大模型
    # gen_result = execute_prompt(s_content, llms.llm_for_gen)
    # print(gen_result)
    # similarity_score = compare(gen_result, d_content, llms.llm_for_gen)
    # print(similarity_score)
    score_list = evalu_main("./dataset4/dataset4_para_protoc.json")
    print(score_list)
    with open("../middle_results/dataset4_para_protoc_score.json", 'w', encoding='utf-8') as f:
        json.dump(score_list, f, ensure_ascii=False, indent=4)


