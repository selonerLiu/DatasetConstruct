import torch
from transformers import AutoTokenizer, AutoModel

# 设置本地模型路径
local_model_path = "/models/Qwen3-Embedding-0.6B"

# 加载 Tokenizer 和 模型（注意：必须信任远程代码）
tokenizer = AutoTokenizer.from_pretrained(local_model_path, trust_remote_code=True)
model = AutoModel.from_pretrained(local_model_path, trust_remote_code=True).eval()

# 判断是否使用 GPU
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Torch CUDA device:{torch.cuda.is_available()}")
print(f"current device:{device}")
model = model.to(device)


# 定义获取嵌入函数
def get_embeddings(texts):
    inputs = tokenizer(texts, padding=True, truncation=True, max_length=512, return_tensors="pt").to(device)
    # 查看运算是否加载到GPU上进行了
    print("Model device after to(device):", next(model.parameters()).device)
    print("Input device after to(device):", inputs["input_ids"].device)
    with torch.no_grad():
        outputs = model(**inputs)
    # 取 [CLS] 向量 或 平均池化所有 token 的向量
    embeddings = outputs.last_hidden_state.mean(dim=1)  # 平均池化
    embeddings = torch.nn.functional.normalize(embeddings, p=2, dim=1)  # L2 归一化
    return embeddings.cpu().numpy()

# 示例文本
texts = [
    "人工智能正在改变世界。",
    "大模型技术发展迅速。",
]

# 获取嵌入向量
embeddings = get_embeddings(texts)
print(embeddings)
print("Embedding shape:", embeddings.shape)
