###Agent核心逻辑
###这里才是真正的Agent Workflow，负责调用工具函数获取网页内容，并将内容传递给DeepSeek进行分析，最后返回分析结果。
from openai import OpenAI
from dotenv import load_dotenv
import os

from Workflow_Engineering.web_agent.tools import get_webpage_content
from Workflow_Engineering.web_agent.prompt import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def run_agent(url):

    print("正在获取网页内容...")

    ###第一步：Agent调用工具函数获取网页内容，这一步就是Tool Calling
    ###第二步LLM开始分析网页内容，这一步就是LLM Reasoning
    webpage_text = get_webpage_content(url)

    print("网页获取成功")
    print("正在调用DeepSeek分析...")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"""
请分析以下网页内容：

{webpage_text}
"""
            }
        ]
    )

    return response.choices[0].message.content