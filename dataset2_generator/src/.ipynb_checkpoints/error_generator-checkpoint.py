import datetime
import json
import os
import random
import re
import subprocess
from pathlib import Path


def invoke_proverif_win(application, file):
    """
    Windows环境下，调用proverif工具编译file文件并返回最终运行结果
    :param application: proverif工具的路径
    :param file: 需要验证的文件
    :return: 返回值和错误信息
    """
    command = application
    arguments = file
    # 使用subprocess.Popen调用.exe文件
    process = subprocess.Popen([command, arguments], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # 获取.exe文件的返回值
    stdout, stderr = process.communicate()
    # 转换返回值的编码
    stdout = stdout.decode('utf-8')
    stderr = stderr.decode('utf-8')
    # 获取.exe文件的返回码，其中0代表正常，其它数字代表错误。
    return_code = process.returncode
    return return_code, stdout, stderr


def invoke_proverif_linux(application_path, input_file):
    """
    在Linux环境下运行ProVerif软件
    :para input_file: 输入文件路径(.pv文件)
    :return: tuple: (返回码, 标准输出, 标准错误)
    """
    # 验证文件是否存在
    if not os.path.exists(input_file):
        return -1, f"错误：文件 {input_file} 不存在", ""
    
    # 如果未全局安装，使用当前目录下的可执行文件
    proverif_path = application_path if os.path.exists(application_path) else "proverif"
    
    # 添加必要的参数
    arguments = [input_file]
    
    # try:
    
    # 使用subprocess.Popen调用proverif
    process = subprocess.Popen(
        [proverif_path] + arguments,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    # 获取输出
    stdout, stderr = process.communicate()
    # 等待进程结束并获取返回码
    return_code = process.returncode
    return return_code, stdout, stderr
    
    # except FileNotFoundError:
    #     return -1, "", f"错误：找不到ProVerif可执行文件。请确保已编译安装"
    # except Exception as e:
    #     return -1, "", f"运行ProVerif时出错: {str(e)}"


def exe_info_process(stdout):
    # 处理proverif的输出信息，提取出精简内容，包括两个部分：错误位置和错误内容
    position_text = stdout
    start_index = position_text.find('.pv", ')
    end_index = position_text.find(':')
    if start_index == -1 or end_index == -1:
        return None
    position_info = position_text[start_index + len('.pv", '):end_index]
    error_message = stdout
    start_index_e = error_message.find('Error: ')
    end_index_e = error_message.rfind('.')
    if start_index_e == -1 or end_index_e == -1:
        return None
    error_info = error_message[start_index_e + len('Error: '):end_index_e]
    return position_info, error_info


def is_in_comment(keyword_index, keyword, text):
    """
    给定关键词位置，判断该关键词是否在注释里面。
    :param keyword: 关键词
    :param keyword_index: 关键词位置
    :param text: 文件内容
    """
    count = 0
    i = 0
    n = len(text)
    # print(text[(keyword_index + 1):(keyword_index + len(keyword) + 1)])
    while i <= keyword_index and i < n:
        # 检查注释开始标记 "(*"
        if i < n - 1 and text[i] == '(' and text[i + 1] == '*':
            count += 1
            i += 2  # 跳过两个字符
            continue

        # 检查注释结束标记 "*)"
        if i < n - 1 and text[i] == '*' and text[i + 1] == ')':
            if count > 0:
                count -= 1
            i += 2  # 跳过两个字符
            continue
        # 普通字符，继续前进
        i += 1
    if count > 0:
        while len(keyword) < i < n:
            # 在关键词之后再检查是否有闭合符号，遇到第一个闭合符号就开始判断，只要遇到我们就认定关键词是在一个闭合的注释内容中，不管其它的是否闭合
            if text[i] == '*' and text[i + 1] == ')':
                count -= 1
                return True
            i += 1
        if count != 0:
            return False
    else:
        # 只要被*)抵销后在，关键词之前没有出现（*符号组合，就认为关键词不可能在注释体内
        return False


def delete_comment(content):
    """
    删除proverif文件中(**)包围住的所有注释内容
    :param content: 原内容
    :return: 删除注释后的文件内容
    """
    result = []
    stack = []
    i = 0
    n = len(content)
    while i < n:
        if i + 1 < n and content[i] == '(' and content[i + 1] == '*':
            stack.append(i)
            i += 2
        elif i + 1 < n and content[i] == '*' and content[i + 1] == ')':
            if stack:
                stack.pop()
            i += 2
        else:
            if not stack:  # 如果栈为空，说明不在注释中，直接添加到结果中
                result.append(content[i])
            i += 1
    print("注释已成功删除。")
    return ''.join(result)


# 设定proverif中的所有关键字
keywords = ['among', 'axiom', 'channel', 'choice', 'clauses', 'const', 'def', 'diff', 'do', 'elimtrue', 'else',
            'equation', 'equivalence', 'event', 'expand', 'fail', 'for', 'forall', 'foreach', 'free', 'fun', 'get',
            'if', 'implementation', 'in', 'inj-event', 'insert', 'lemma', 'let', 'letfun', 'letproba', 'new',
            'noninterf', 'noselect', 'not', 'nounif', 'or', 'otherwise', 'out', 'param', 'phase', 'pred', 'proba',
            'process', 'proof', 'public' 'vars', 'putbegin', 'query', 'reduc', 'restriction', 'secret', 'select',
            'set', 'suchthat', 'sync', 'table', 'then', 'type', 'weaksecret', 'yield']


def rule1(raw_correct_file_path):
    """
    设定规则1：关键字错误，随机修改、删除字母、添加字母
    :param raw_correct_file_path: 输入源形式化文件
    :return:各种相关信息
    """
    operation = ""

    """文件准备工作"""
    # 读取文件内容
    try:
        with open(raw_correct_file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
    except FileNotFoundError:
        print(f"错误：文件 '{raw_correct_file_path}' 不存在。")
    except Exception as e:
        print(f"读取文件时发生错误：{e}")

    """规则实现过程"""
    # 随机选一个keywords
    keyword = random.choice(keywords)
    # 在文件中查找该keyword的所有位置用一个列表记录，起始终止index来表示一个关键字，如果不存在则重新选择一个关键词，直到找到为止；然后修改文件中其中一个位置的关键词随机选择增删改任一字母的方式完成修改
    while True:
        # 外层循环用于判断选中的关键词是否在注释里面，如果是则直接另外再选一个关键词再进入内层循环
        while True:
            # 内层循环用于确定所选的关键字在这个文件中存在，若有多个随机选定一个位置
            keyword_index_list = []
            for i in range(len(file_content)):
                if file_content[i:i + len(keyword)] == keyword:
                    keyword_index_list.append(i)
            if len(keyword_index_list) == 0:
                keyword = random.choice(keywords)
            else:
                break
        # 随机选择一个位置的关键词，然后随机使用增删改查的一种方法修改这个关键词
        keyword_index = random.choice(keyword_index_list)
        if is_in_comment(keyword_index, keyword, file_content):
            keyword = random.choice(keywords)
        else:
            break

    if random.random() < 0.33:
        # 增加一个字母
        file_tuned = file_content[:keyword_index + len(keyword)] + random.choice(
            'abcdefghijklmnopqrstuvwxyz') + file_content[keyword_index + len(keyword):]
        operation = "add"
    elif random.random() < 0.66:
        # 删除一个字母
        file_tuned = file_content[:keyword_index] + file_content[keyword_index + 1:]
        operation = "delete"
    else:
        # 修改一个字母
        file_tuned = file_content[:keyword_index] + random.choice('abcdefghijklmnopqrstuvwxyz') + file_content[
                                                                                                  keyword_index + 1:]
        operation = "modify"
    # print(keyword)
    # print(keyword_index)
    # print(operation)

    """改后内容后处理"""
    # 将修改过关键词的文件存入output/witherr_file/路径下，文件名设置为raw_correct_file基础上加上"_err"
    output_dir = "../output/with_err_files"
    filename = os.path.splitext(os.path.basename(raw_correct_file_path))[0]
    output_path = output_dir + f"/{filename}_rule1err1.pv"
    # 确保目录存在
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w") as f:
        f.write(file_tuned)

    """数据集信息收集与存储工作"""
    # 调用proverif工具编译文件并返回最终运行结果
    return_code, stdout, stderr = invoke_proverif_linux("../proverif-linux/proverif", output_path)
    if return_code == 0:
        has_error = "False"
        return raw_correct_file_path, output_path, return_code, has_error, "", "", keyword, f"the error star index is:{keyword_index}"
    else:
        has_error = "True"
        position_info_run, error_info_run = exe_info_process(stdout)
        return raw_correct_file_path, output_path, return_code, has_error, position_info_run, error_info_run, keyword, f"the error star index is:{keyword_index}"


def rule2(raw_correct_file_path):
    """
    设定规则2：随机删除一个类型声明语句，产生未定义错误
    :param raw_correct_file_path:输入源形式化文件
    :return:
    """
    """文件准备工作"""
    # 读取文件内容
    with open(raw_correct_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    # 删除注释
    content = delete_comment(content)

    """规则实现过程"""
    # 使用正则表达式匹配形式化文件中的声明语句
    pattern = r'^.*?\.(?:\s*\n|$)'  # 多行模式匹配每个声明
    declarations = list(re.finditer(pattern, content, re.MULTILINE | re.DOTALL))
    if not declarations:
        return content
    # 随机选择一个声明
    # valid_declarations = declarations[:-1]  # 不删除最后一个进程声明
    # if not valid_declarations:
    #     valid_declarations = declarations  # 如果只有一个声明则直接使用
    chosen = random.choice(declarations)
    # 构建删除后的内容
    err_start_set = chosen.start()
    err_end_set = chosen.end()
    err_info_set = content[err_start_set:err_end_set]
    # print(err_info_set)
    modified_content = content[:err_start_set] + content[err_end_set:]
    # print(modified_content)

    """改后内容后处理"""
    # 将修改过关键词的文件存入output/witherr_file/路径下，文件名设置为raw_correct_file基础上加上"_err"
    # 构建置错文件的输出路径
    output_dir = "../output/with_err_files"
    filename = os.path.splitext(os.path.basename(raw_correct_file_path))[0]
    output_path = output_dir + f"/{filename}_rule2err1.pv"
    # 确保目录存在
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w") as f:
        f.write(modified_content)

    """数据集信息收集与存储工作"""
    # 调用proverif工具编译文件并返回最终运行结果
    return_code, stdout, stderr = invoke_proverif_linux("../proverif-linux/proverif", output_path)
    if return_code == 0:
        has_error = "False"
        return raw_correct_file_path, output_path, return_code, has_error, "", "", err_info_set, f"the error star index is:{err_start_set}"
    else:
        has_error = "True"
        position_info_run, error_info_run = exe_info_process(stdout)
        return raw_correct_file_path, output_path, return_code, has_error, position_info_run, error_info_run, err_info_set, f"the error star index is:{err_start_set}"


def rule3(raw_correct_file_path):
    """
    设定规则3：随机修改一个符号。注释错、分号缺、括号不闭合、process结束语句多句点等类型。
    :param raw_correct_file_path:输入源形式化文件
    :return:null
    """
    """文件准备工作"""
    # 读取文件内容
    try:
        with open(raw_correct_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"错误：文件 '{raw_correct_file_path}' 不存在。")
    except Exception as e:
        print(f"读取文件时发生错误：{e}")

    """规则实现过程"""
    new_content = ""
    err_info_set = ""
    err_position_set = ""
    rand_num = random.random()
    if rand_num <= 0.33:
        print("修改注释")
        # 注释符号修改：随机选择一对(*，修改成//或"""，或#。目前实现修改为"""注释
        stack = []
        index_list = []
        n = len(content)
        i = 0
        for i in range(len(content)):
            if content[i] == '(' and content[i + 1] == '*':
                stack.append(i + 1)
                stack.append(i)
            elif content[i] == '*' and content[i + 1] == ')':
                if stack:
                    index_list.append(stack.pop())
                    index_list.append(stack.pop())
                    index_list.append(i)
                    index_list.append(i + 1)
        if index_list:
            # print(index_list)
            valid_indices = [idx for idx in range(len(index_list)) if idx % 4 == 0]
            index = random.choice(valid_indices)  # 选择一个4的倍数的注释起始位置
            one_comment_list = index_list[index:index + 4]  # 后面连续4个字符表示一套注释索引
            # print(one_comment_list)
            pre_content = content[:one_comment_list[0]]
            post_content = content[one_comment_list[3] + 1:]
            comment = content[one_comment_list[1] + 1:one_comment_list[2]]

            new_content = pre_content + '"""' + comment + '"""' + post_content
            err_position_set = f"the error star index is: {one_comment_list[0]}"
            err_info_set = content[one_comment_list[0]:one_comment_list[3] + 1]
        else:
            new_content = '\"\"\"for the format file that has no comment, just add a comment that do not use the right method\"\"\"' + content
            err_position_set = f"the error star index is: 0"
            err_info_set = "the first line comment"
        print(len(new_content))

    elif 0.33 < rand_num <= 0.66:
        print("修改分号")
        # 分号修改：随机选择一个不在注释内的分号，将其删除
        semicolon_indices = [i for i in range(len(content)) if content[i] == ';']
        # 如果文件中没有分号, 或者只有一个分号且在注释体里，则在文本最后加上一个分号
        if not semicolon_indices:
            new_content = content + ";"
            err_position_set = f"the error star index is: {len(content)}"
            err_info_set = "there is an redundant semicolon ';' in the end of the file"

        else:  # 否则随机选择一个删除掉。
            semicolon_index = random.choice(semicolon_indices)
            i = 0
            while is_in_comment(semicolon_index, ";", content) and i<5:
                i += 1
                print("in the comment, random select once more")
                semicolon_index = random.choice(semicolon_indices)
            new_content = content[:semicolon_index] + content[semicolon_index + 1:]
            err_position_set = f"the error star index is: {semicolon_index}"
            err_info_set = ";"
        print(len(new_content))

    elif 0.66 < rand_num <= 1:
        print("修改括号闭合性")
        # 括号闭合性：随机选择一对()、[]删除左或右括号，使其不完整
        stack_1 = []
        stack_2 = []
        index_list = []  # 用以记录所有正常闭合符号的索引
        for i in range(len(content)):
            if content[i] == '(' and content[i + 1] != '*':
                stack_1.append(i)
            elif content[i] == '[':
                stack_2.append(i)
            elif content[i] == ')' and content[i - 1] != '*':
                if stack_1:
                    index_list.append(stack_1.pop())
                    index_list.append(i)
            elif content[i] == ']':
                if stack_2:
                    index_list.append(stack_2.pop())
                    index_list.append(i)
        # 随机从index_list中取一个索引值
        index = random.choice(index_list)
        new_content = content[:index] + content[index + 1:]
        err_position_set = f"the error star index is: {index}"
        err_info_set = content[index:index + 1]

        print(len(new_content))
    # 进程语句修改：在process后添加一个句点，一个文件只有一个进程
    # 进程内计算符号修改：

    """改后内容后处理"""
    # 将修改过关键词的文件存入output/witherr_file/路径下，文件名设置为raw_correct_file基础上加上"_err"
    # 构建置错文件的输出路径
    output_dir = "../output/with_err_files"
    filename = os.path.splitext(os.path.basename(raw_correct_file_path))[0]
    output_path = output_dir + f"/{filename}_rule3err1.pv"
    # 确保目录存在
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w") as f:
        f.write(new_content)

    """数据集信息收集与存储工作"""
    # 调用proverif工具编译文件并返回最终运行结果
    return_code, stdout, stderr = invoke_proverif_linux("../proverif-linux/proverif", output_path)
    if return_code == 0:
        has_error = "False"
        return raw_correct_file_path, output_path, return_code, has_error, "", "", err_info_set, err_position_set
    else:
        has_error = "True"
        position_info_run, error_info_run = exe_info_process(stdout)
        return raw_correct_file_path, output_path, return_code, has_error, position_info_run, error_info_run, err_info_set, err_position_set


def rule4(raw_correct_file_path):
    """
    设定规则4：函数使用与定义时的参数数量或类型不匹配。
    :param raw_correct_file_path:输入源形式化文件
    :return:null
    """
    """文件准备工作"""
    # 按行读入文件

    try:
        with open(raw_correct_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"错误：文件 '{raw_correct_file_path}' 不存在。")
    except Exception as e:
        print(f"读取文件时发生错误：{e}")

    """规则实现过程"""
    # 查找函数定义位置，通过直接修改函数原定义类型和参数数量来产生与使用时不一致的错误现象
    # 在content中查找函数定义语句
    func_list = []
    for index, line in enumerate(lines):
        # print(index, line)
        if line.startswith("fun "):
            func_list.append({"line": index, "content": line})
    # # 随机选择一个函数定义,对其进行修改
    new_line = ""
    new_content = ""
    err_info_set = "the parameters number of the function invoked is not equal to the definition"
    err_position_set = ""
    if func_list:
        func_select = random.choice(func_list)
        # print(func_select)
        line_num_selected = func_select["line"]
        line_content_selected = func_select["content"]
        stack = []
        # 对当前选中行的函数进行字符级操作，若有多个参数删除最后一个，若只有一个参数，在最后添加一个paraadded参数
        for i in range(len(line_content_selected)):
            if line_content_selected[i] in ['(', ',', ')']:
                stack.append(i)
        right_plural = 0
        if len(stack) > 2:
            right_plural = stack.pop()
            last_dot = stack.pop()
            new_line = line_content_selected[:last_dot] + line_content_selected[right_plural:]
        elif len(stack) == 2:
            right_plural = stack.pop()
            new_line = line_content_selected[:right_plural] + " ,paraadded" + line_content_selected[right_plural:]
        # print(new_line)
        # 用修改过的行替换原行，重新输出原文件
        new_content_lines = []
        for index, line in enumerate(lines):
            if index == line_num_selected:
                new_content_lines.append(new_line)
            else:
                new_content_lines.append(line)
        new_content = ''.join(new_content_lines)
        err_info_set = "the parameters number of the function invoked is not equal to the definition"
        err_position_set = f"line: {line_num_selected}, column: {right_plural}"
        # print(new_content)
    else:
        print("No function definition found in the file.")

    """改后内容后处理"""
    # 将修改过关键词的文件存入output/witherr_file/路径下，文件名设置为raw_correct_file基础上加上"_err"
    # 构建置错文件的输出路径
    output_dir = "../output/with_err_files"
    filename = os.path.splitext(os.path.basename(raw_correct_file_path))[0]
    output_path = output_dir + f"/{filename}_rule4err1.pv"
    # 确保目录存在
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w") as f:
        f.write(new_content)

    """数据集信息收集与存储工作"""
    # 调用proverif工具编译文件并返回最终运行结果
    return_code, stdout, stderr = invoke_proverif_linux("../proverif-linux/proverif", output_path)
    if return_code == 0:
        has_error = "False"
        return raw_correct_file_path, output_path, return_code, has_error, "", "", err_info_set, err_position_set
    else:
        has_error = "True"
        position_info_run, error_info_run = exe_info_process(stdout)
        return raw_correct_file_path, output_path, return_code, has_error, position_info_run, error_info_run, err_info_set, err_position_set


def rule5(raw_correct_file_path):
    """
    设定规则5：系统改变类型定义。查找所有非关键词的字母，全部字母ASCII码值加1
    :param raw_correct_file_path:输入源形式化文件
    :return:null
    """
    """文件准备工作"""
    # 读取文件内容
    try:
        with open(raw_correct_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"错误：文件 '{raw_correct_file_path}' 不存在。")
    except Exception as e:
        print(f"读取文件时发生错误：{e}")

    """规则实现过程"""
    # 获取所有不该变字母的索引，遍历所有关键词，每一个关键词与文本匹配一遍文本，能够对应上的地方的索引值加入一个list中
    all_keyword_index = []
    keywords_ext = keywords + ["True", "False", "true", "false", "attacker", "bitstring", "data", "private", "typeConverter", "projection", "uniform"]
    for keyword in keywords_ext:
        positions = []
        start = 0
        while True:
            idx = content.find(keyword, start)
            if idx == -1:
                break
            # 记录这个关键词占据的所有索引位置
            indices = list(range(idx, idx + len(keyword)))
            positions = positions + indices
            # positions.append(indices)
            start = idx + 1  # 移动指针继续查找
        # if positions:
        #     print(keyword, positions)
        all_keyword_index = all_keyword_index + positions
        # all_keyword_index.append(positions)

    # 将text中所有indices以外的索引位置字母asc码都加1
    index_set = set(all_keyword_index)
    result = []
    for i, char in enumerate(content):
        char_asc_base = ord('a') if char.islower() else ord('A')
        if i in index_set:
            # 如果当前索引在指定位置中，保留原字符
            result.append(char)
        else:
            # 否则检查是否为字母
            if char.isalpha():
                # 将字符的ASCII码加1
                result.append(chr((ord(char) - char_asc_base + 1) % 26 + char_asc_base))
            else:
                # 非字母字符保持不变
                result.append(char)
    new_content = "".join(result)

    """改后内容后处理"""
    # 将修改过关键词的文件存入output/witherr_file/路径下，文件名设置为raw_correct_file基础上加上"_err"
    # 构建置错文件的输出路径
    output_dir = "../output/with_err_files"
    filename = os.path.splitext(os.path.basename(raw_correct_file_path))[0]
    output_path = output_dir + f"/{filename}_rule5err1.pv"
    # 确保目录存在
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w") as f:
        f.write(new_content)

    """数据集信息收集与存储工作"""
    # 调用proverif工具编译文件并返回最终运行结果
    return_code, stdout, stderr = invoke_proverif_linux("../proverif-linux/proverif", output_path)
    if return_code == 0:
        has_error = "False"
        return raw_correct_file_path, output_path, return_code, has_error, "", "", "all index of letters that are not keywords", "all letters that are not keywords"
    else:
        has_error = "True"
        position_info_run, error_info_run = exe_info_process(stdout)
        return raw_correct_file_path, output_path, return_code, has_error, position_info_run, error_info_run, "all index of letters that are not keywords", "all letters that are not keywords"


def generator_main(file_dir, dataset2_dir):
    """
    生成数据集
    :param file_dir:原始形式化文件的存储目录
    :param dataset2_dir: 目标数据集的存储目录
    :return:null
    """
    # 读取文件列表
    file_list = os.listdir(file_dir)

    # 对每个文件执行rule1，每执行一个rule产生一条json数据，src_path,dst_path,run_code, err_position_run, err_message_run, err_keyword_set, err_index_set.将数据添加到一个列表中
    results = []
    for file in file_list:
        file_path = file_dir + "/" + file
        print(f"🔄 正在使用5种不同规则处理文件：{file_path}")
        # 调用rule1函数，返回修改后的文件路径和错误信息
        src_path, dst_path, run_code, has_err, err_position_run, err_message_run, err_keyword_set, err_index_set = rule1(
            file_path)
        result = {
            "src_path": src_path, "dst_path": dst_path, "run_code": run_code,
            "err_position_run": err_position_run, "err_message_run": err_message_run, "has_err": has_err,
            "err_keyword_set": err_keyword_set, "err_index_set": err_index_set}
        results.append(result)
        print(f"基于rule1已修改{file_path}文件，修改后的文件已存入{dst_path}")

        # 调用rule2函数，返回修改后的文件路径和错误信息
        src_path, dst_path, run_code, has_err, err_position_run, err_message_run, err_keyword_set, err_index_set = rule2(
            file_path)
        result = {
            "src_path": src_path, "dst_path": dst_path, "run_code": run_code,
            "err_position_run": err_position_run, "err_message_run": err_message_run, "has_err": has_err,
            "err_keyword_set": err_keyword_set, "err_index_set": err_index_set}
        results.append(result)
        print(f"基于rule2已修改{file_path}文件，修改后的文件已存入{dst_path}")

        # 调用rule3函数，返回修改后的文件路径和错误信息
        src_path, dst_path, run_code, has_err, err_position_run, err_message_run, err_keyword_set, err_index_set = rule3(
            file_path)
        result = {
            "src_path": src_path, "dst_path": dst_path, "run_code": run_code,
            "err_position_run": err_position_run, "err_message_run": err_message_run, "has_err": has_err,
            "err_keyword_set": err_keyword_set, "err_index_set": err_index_set}
        results.append(result)
        print(f"基于rule3已修改{file_path}文件，修改后的文件已存入{dst_path}")

        # 调用rule4函数，返回修改后的文件路径和错误信息
        src_path, dst_path, run_code, has_err, err_position_run, err_message_run, err_keyword_set, err_index_set = rule4(
            file_path)
        result = {
            "src_path": src_path, "dst_path": dst_path, "run_code": run_code,
            "err_position_run": err_position_run, "err_message_run": err_message_run, "has_err": has_err,
            "err_keyword_set": err_keyword_set, "err_index_set": err_index_set}
        results.append(result)
        print(f"基于rule4已修改{file_path}文件，修改后的文件已存入{dst_path}")

        # 调用rule5函数，返回修改后的文件路径和错误信息
        src_path, dst_path, run_code, has_err, err_position_run, err_message_run, err_keyword_set, err_index_set = rule5(
            file_path)
        result = {
            "src_path": src_path, "dst_path": dst_path, "run_code": run_code,
            "err_position_run": err_position_run, "err_message_run": err_message_run, "has_err": has_err,
            "err_keyword_set": err_keyword_set, "err_index_set": err_index_set}
        results.append(result)
        print(f"基于rule5已修改{file_path}文件，修改后的文件已存入{dst_path}")

    # 将获取的文件路径和错误信息写入json文件
    timestamp = datetime.datetime.now().strftime("%Y-%m%d-%H%M%S")
    Path(dataset2_dir).mkdir(parents=True, exist_ok=True)
    dataset2_path = dataset2_dir + f"/dataset2_{timestamp}.json"
    with open(dataset2_path, "a") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # # 测试rule1函数功能
    # src_path, dst_path, run_code, has_err, err_position_run, err_message_run, err_keyword_set, err_index_set = rule1(
    #     "../checked_raw_files/DiffieHellman-active.pv")

    # # 测试linux下调用proverif方法 
    # a,b,c = invoke_proverif_linux("../proverif-linux/proverif", "../output/with_err_files/WooLamSK_rule1err1.pv")
    # print(a)
    # print(b)

    # # 测试删除注释功能
    # with open("../checked_raw_files/EKE.pv", 'r', encoding='utf-8') as file:
    #     file_content = file.read()
    # result = delete_comment(file_content)
    # print(result)

    # # 测试rule2函数功能
    # mdf_content = rule2("../checked_raw_files/EKE.pv")

    # # rule3函数功能测试
    # symbol_modify = rule3("../checked_raw_files/EKE.pv")
    # print(symbol_modify)

    # # 测试rule4函数功能
    # rule4("../checked_raw_files/EKE.pv")

    # # 测试rule5函数功能
    # rule5("../checked_raw_files/EKE.pv")

    # 测试生成主函数的功能
    generator_main("../checked_raw_files", "../output/dataset_remote")
