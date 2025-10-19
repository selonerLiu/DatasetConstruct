import yaml
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain.schema.runnable import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import OpenAIEmbeddings
import logging

logger = logging.getLogger(__name__)


class RAGEngine:
    def __init__(self, vectorstore_dir="../data/vectorstore", settings_dir="../config/settings.yaml"):
        with open(settings_dir, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
            self.embed_api_key = config["embed_api_key"]
            self.embed_api_base = config["embed_api_base"]
            self.embed_model_name = config["embed_model_name"]
            self.refer_api_key = config["refer_api_key"]
            self.refer_api_base = config["refer_api_base"]
            self.refer_model_name = config["refer_model_name"]
        embeddings = OpenAIEmbeddings(model=self.embed_model_name, openai_api_base=self.embed_api_base,
                                      openai_api_key=self.embed_api_key)
        self.vectorstore = FAISS.load_local(vectorstore_dir, embeddings, allow_dangerous_deserialization=True)
        self.retriever = self.vectorstore.as_retriever(search_kwargs={"k": 10})  # 每次检索10个相关段落
        self.llm = ChatOpenAI(model_name=self.refer_model_name, openai_api_base=self.refer_api_base,
                              openai_api_key=self.refer_api_key)

    def _format_docs(self, docs):
        return "*****\n".join(doc.page_content for doc in docs)


    def inspect(self, item):
        # 用于监测chain执行链中间过程产生的结果
        print("🔍 中间内容:", item)
        return item


    def create_chain(self):
        """构建RAG链式调用"""
        prompt = PromptTemplate(
            input_variables=["context", "topic"],
            template="""
                Suppose you are a teacher. Please design 10 multiple-choice questions based on the following content 
                to test whether your students have fully understood the following topic". 
                content：{context}
                topic：{topic}
                demands：
                1. The question should be clearly described.
                2. the options should be plausible distractors.
                3. The answer should be clearly stated(eg. answer：B).
                4. Each question should be different.
                5. The format of questions should be consist with the following example:
                    ---
                    **1.In the given formalism, what must be done before using a variable or a name in a process declaration?**
                    A) It can be used without prior declaration.  
                    B) It must be declared with its type before use.  
                    C) It must be declared only if used in a conditional statement.  
                    D) Declaration is optional for free names.  
                    **Answer:** B
                    ---
                """)

        chain = (
                {"context": self.retriever | self._format_docs,
                 "topic": RunnablePassthrough()}  # 将retriver返回的几个内容传给_format_docs函数拼接成一个串，context键对应的值就是这个串。RunnablePassthrough直接透传原始问题不做处理，原始是调用chain.stream的时候传进来的。
                | prompt  # 以上步骤生成的字典直接传入prompt，prompt会根据字典中的键值对生成一个字符串
                | self.inspect
                | self.llm  # 将prompt生成的字符串传给llm，llm会根据这个增强的prompt生成一个结果字符串
                | StrOutputParser()  # 模型输出的AIMessage转换为纯文本字符串
        )
        return chain


if __name__ == "__main__":
    rag = RAGEngine()
    rag_chain = rag.create_chain()
    for chunk in rag_chain.invoke("syntactic knowledge about how to write a construction using proverif"):  # chain.stream将参数值传给chain里面的第一个处理流程retriever
        print(chunk, end="", flush=True)
        break

