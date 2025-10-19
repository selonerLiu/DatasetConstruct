import subprocess
import os
import datetime
import json
from pathlib import Path
import shutil


def run_pv_files(collected_rawfile_dir, checked_rawfile_dir, executable="proverif.exe"):
    results = []
    dir_path = Path(collected_rawfile_dir)
    Path(checked_rawfile_dir).mkdir(parents=True, exist_ok=True)
    # 确保路径存在
    if not dir_path.exists() or not dir_path.is_dir():
        raise FileNotFoundError(f"源文件目录不存在: {collected_rawfile_dir}")
    # 遍历目录下所有 .pv 文件
    i = 0
    for file_path in dir_path.rglob("*.pv"):
        i += 1
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 执行 proverif.exe 并捕获输出
        print(f"🔄 正在执行文件{i}: {file_path}")

        try:
            # 启动进程并捕获 stdout 和 stderr
            process = subprocess.run(
                [executable, str(file_path)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='utf-8',
                errors='replace'  # 处理乱码
            )
            # 记录输出和错误信息
            result = {
                "exectime": timestamp,
                "filename": str(file_path),
                "stdout": process.stdout,
                "stderr": process.stderr,
                "returncode": process.returncode
            }
            print(f"💎 执行结果代码是：{process.returncode}")
            # 如果执行成功（返回码为 0），则复制文件到 dir2
            if process.returncode == 0:
                dest_file = Path(checked_rawfile_dir) / file_path.name
                shutil.copy(str(file_path), dest_file)
                print(f"✅ 成功执行并复制文件: {file_path} -> {dest_file}")
            else:
                print("⚠️  此文件有问题，不复制")
            results.append(result)

        except Exception as e:
            print(f"执行失败: {str(file_path)}, 错误: {e}")
            results.append({
                "filename": str(file_path),
                "error": str(e)
            })
    return results


if __name__ == '__main__':
    results = run_pv_files("../collected_raw_file/demos", "./checked_raw_files",
                           executable="./proverif2.05/proverif.exe")
    output_dir = "../output/"
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    file_path = output_dir + "exec_results.json"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(results, ensure_ascii=False, indent=4))
