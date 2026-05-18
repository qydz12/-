###程序入口
from Workflow_Engineering.web_agent.agent import run_agent

url = input("请输入网址: ")

result = run_agent(url)

print("\n====== 分析结果 ======\n")

print(result)