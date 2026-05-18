###Workflow控制
###Agent的职责是先干什么、再干什么、数据怎么流动。
###在这个文件中，我们定义了Agent的核心逻辑，控制整个分析流程。Agent首先调用工具函数获取新闻内容，然后清洗文本，最后将清洗后的文本传递给DeepSeek进行分析，并返回分析结果。
# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# from search import search_news
# from tools import get_news_content
# from cleaner import clean_text
# from prompts import SYSTEM_PROMPT

# load_dotenv()

# client = OpenAI(
#     api_key=os.getenv("DEEPSEEK_API_KEY"),
#     base_url="https://api.deepseek.com"
# )

# def run_news_agent(topic):

#     print("正在搜索相关新闻...")

#     urls = search_news(topic)

#     if not urls:
#         return "没有找到相关新闻"

#     all_news = ""

#     for url in urls:

#         print(f"正在分析: {url}")

#         raw_text = get_news_content(url)

#         cleaned_text = clean_text(raw_text)

#         all_news += cleaned_text + "\n\n"

#     print("正在调用DeepSeek分析...")

#     response = client.chat.completions.create(
#         model="deepseek-chat",
#         messages=[
#             {
#                 "role": "system",
#                 "content": SYSTEM_PROMPT
#             },
#             {
#                 "role": "user",
#                 "content": f"""
# 请分析以下新闻内容：

# {all_news}
# """
#             }
#         ]
#     )

#     return response.choices[0].message.content

# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# from Workflow_Engineering.News_Agent.search import search_news
# from Workflow_Engineering.News_Agent.prompts import SYSTEM_PROMPT


# load_dotenv()

# client = OpenAI(
#     api_key=os.getenv("DEEPSEEK_API_KEY"),
#     base_url="https://api.deepseek.com"
# )

# def run_news_agent(topic):

#     print("正在搜索最新新闻...")

#     news_results = search_news(topic)

#     if not news_results:
#         return "没有找到相关新闻"

#     all_news = ""

#     for news in news_results:

#         title = news["title"]
#         content = news["content"]
#         url = news["url"]

#         all_news += f"""
# 标题:
# {title}

# 内容:
# {content}

# 来源:
# {url}

# ====================
# """

#     print("正在调用DeepSeek分析...")

#     response = client.chat.completions.create(
#         model="deepseek-chat",
#         messages=[
#             {
#                 "role": "system",
#                 "content": SYSTEM_PROMPT
#             },
#             {
#                 "role": "user",
#                 "content": f"""
# 请分析以下最新新闻：

# {all_news}
# """
#             }
#         ]
#     )

#     return response.choices[0].message.content

###升级版
from openai import OpenAI
from dotenv import load_dotenv
import os

from search import search_news

from filters import (
    filter_by_source,
    deduplicate_news
)

from ranking import calculate_news_score

from prompts import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def run_news_agent(topic):

    print("正在搜索最新新闻...")

    # 1. 搜索新闻
    news_results = search_news(topic)

    print(f"原始新闻数量: {len(news_results)}")

    # 2. 来源过滤
    news_results = filter_by_source(news_results)

    print(f"来源过滤后: {len(news_results)}")

    # 3. 去重
    news_results = deduplicate_news(news_results)

    print(f"去重后: {len(news_results)}")

    # 4. 新闻评分
    for news in news_results:

        news["final_score"] = calculate_news_score(news, topic)

    # 5. 新闻排序
    news_results = sorted(
        news_results,
        key=lambda x: x["final_score"],
        reverse=True
    )

    print("新闻评分排序完成")

    all_news = ""

    # 6. 拼接新闻
    for news in news_results:

        title = news.get("title", "")
        content = news.get("content", "")
        url = news.get("url", "")
        score = news.get("final_score", 0)

        all_news += f"""
新闻标题:
{title}

新闻内容:
{content}

新闻来源:
{url}

新闻评分:
{score}

====================
"""

    print("正在调用DeepSeek分析...")

#     # 7. LLM分析
#     response = client.chat.completions.create(
#         model="deepseek-chat",

#         messages=[
#             {
#                 "role": "system",
#                 "content": SYSTEM_PROMPT
#             },

#             {
#                 "role": "user",
#                 "content": f"""
# 请分析以下高质量最新新闻：

# {all_news}
# """
#             }
#         ]
#     )

#     return response.choices[0].message.content
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
    当前新闻主题：

    {topic}

    请围绕这个主题：

    1. 提取最重要新闻
    2. 分析核心事件
    3. 分析趋势
    4. 分析影响
    5. 提取关键信号

    以下是相关新闻内容：

    {all_news}
    """
            }
        ]
    )
    return response.choices[0].message.content