import yaml
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_chroma import Chroma
import os
import logging

from tqdm import tqdm

logger = logging.getLogger(__name__)

class PDFProcessor:
    def __init__(self, pdf_dir="../data/raw_pdfs", vectorstore_dir="../data/vectorstore", settings_dir="../config/settings.yaml"):
        self.pdf_dir = pdf_dir
        self.vectorstore_dir = vectorstore_dir
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=96)
        with open(settings_dir, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
            self.openai_api_key = config["openai_api_key"]
            self.openai_api_base = config["openai_api_base"]
            self.embed_model_name = config["embed_model_name"]

    def load_pdfs(self):
        """加载所有PDF文件并分割成文本块"""
        documents = []
        for file in os.listdir(self.pdf_dir):
            if file.endswith(".pdf"):
                loader = PyPDFLoader(os.path.join(self.pdf_dir, file))
                docs = loader.load()
                documents.extend(self.text_splitter.split_documents(docs))
        return documents

    def create_vectorstore(self):
        """创建向量数据库并持久化"""
        documents = self.load_pdfs()
        # embeddings = OpenAIEmbeddings(model=self.embed_model_name, openai_api_base=self.openai_api_base,
        #                               openai_api_key=self.openai_api_key)
        # # 以下是使用FAISS存储的方法，目前还没正确存储，需要再调试
        # vectorstore = FAISS.from_documents(documents, embeddings)
        # vectorstore.save_local(self.vectorstore_dir)

        # 使用 tqdm 包装嵌入函数，显示进度条。这个进度显示只有初始和最终状态，有待完善……
        class ProgressEmbeddings:
            def __init__(self, embeddings):
                self.embeddings = embeddings
                self.pbar = None

            def embed_documents(self, texts):
                if not self.pbar:
                    self.pbar = tqdm(total=len(texts), desc="📄嵌入文档中")
                result = self.embeddings.embed_documents(texts)
                self.pbar.update(len(texts))
                return result

            def embed_query(self, text):
                return self.embeddings.embed_query(text2=text)
        # 初始化嵌入模型 + 进度包装器
        embeddings = OpenAIEmbeddings(model=self.embed_model_name,
                                      openai_api_base=self.openai_api_base,
                                      openai_api_key=self.openai_api_key)
        wrapped_embeddings = ProgressEmbeddings(embeddings)
        # 创建向量库（使用带进度的嵌入模型）
        vectorstore = FAISS.from_documents(documents, wrapped_embeddings)
        vectorstore.save_local(self.vectorstore_dir)


if __name__ == "__main__":
    processor = PDFProcessor(pdf_dir="../data/raw_pdfs", vectorstore_dir="../data/vectorstore", settings_dir="../config/settings.yaml")
    processor.create_vectorstore()
    print("Vectorstore created successfully!")
