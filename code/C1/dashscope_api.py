import os

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

# 读取本地/项目的环境变量。
# find_dotenv()寻找并定位.env文件的路径
# load_dotenv()读取该.env文件，并将其中的环境变量加载到当前的运行环境中
# 如果你设置的是全局的环境变量，这行代码则没有任何作用。
load_dotenv(find_dotenv())

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 传入单条消息 
def get_completion(prompt, model="qwen-plus", temperature=0.0):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature, # 模型输出的温度系数，控制输出的随机程度
    )
    return response.choices[0].message.content 

# 传入多条消息 messages
def get_completion_from_messages(messages, model="qwen-plus", temperature=0.0):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature, # 控制模型输出的随机程度
    )
    return response.choices[0].message.content

# 测试
if __name__ == "__main__":
    print(get_completion("你是谁？"))

