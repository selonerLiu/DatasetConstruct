import logging
import time

import yaml
from pathlib import Path

logger = logging.getLogger(__name__)

class QuestionGenerator:
    def __init__(self, config_path="../config/topics.yaml"):
        with open(config_path, "r", encoding="utf-8") as f:
            self.topics = yaml.safe_load(f)  # 加载知识点配置

    def generate_questions(self, rag_chain, output_dir=""):
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        for topic, description in self.topics.items():
            questions = []
            # for i in range(1, 21):  # 每个知识点生成20题
            print(f"******关于{topic}题目制作中***************************************")
            query = f"{description}"
            result = rag_chain.invoke(query)
            print(result)
            questions.append(result)

            # 保存到文件
            with open(f"{output_dir}/{topic}.md", "w", encoding="utf-8") as f:
                f.write(f"# topic：{description}\n\n")
                f.write("\n\n".join(questions))

            # time.sleep(30)  # 在使用Kimi进行生成的时候流量限制较大，每分钟有访问次数和Token数量限制，因此加一个时间延迟，确保能够连续访问。
