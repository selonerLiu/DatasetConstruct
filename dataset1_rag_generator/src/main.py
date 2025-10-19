from dataset1_rag_generator.src.data_processor import PDFProcessor
from dataset1_rag_generator.src.merge_files import merge_mdfile, merge_json_files
import os
import logging
from datetime import datetime

from dataset1_rag_generator.src.question_generator import QuestionGenerator
from dataset1_rag_generator.src.rag_engine import RAGEngine


def main():
    # 设置日志目录和文件名
    log_dir = "../output/logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"rag_exam_generator_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    # 配置 logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()  # 同时输出到控制台
        ]
    )

    # 1. 数据预处理（首次运行需启用，后续可注释）
    processor = PDFProcessor(pdf_dir="../data/raw_pdfs", vectorstore_dir="../data/vectorstore")
    processor.create_vectorstore()

    # 2. 初始化RAG引擎，初始化的时候设定推理大模型参数，
    rag_engine = RAGEngine()
    rag_chain = rag_engine.create_chain()

    # 3. 生成试题，每个主题存储在一个md文件中，所使用的问题嵌入模型和问题生成模型均可在setting文件中修改
    generator = QuestionGenerator()
    generator.generate_questions(rag_chain, output_dir="../output/exams/llm8")

    # 4. 试题转换为数据集json存储
    merge_mdfile("../output/exams/llm8/", "../output/qa_set/questions-llm8.json")


if __name__ == "__main__":
    main()
