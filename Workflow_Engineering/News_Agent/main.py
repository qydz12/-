###用户入口
# from Workflow_Engineering.News_Agent.agent import run_news_agent

# topic = input("请输入新闻主题: ")

# result = run_news_agent(topic)

# print("\n====== 新闻分析结果 ======\n")

# print(result)


###升级版

from agent import run_news_agent

topic = input("请输入新闻主题: ")

result = run_news_agent(topic)

print("\n====== AI新闻情报分析 ======\n")

print(result)