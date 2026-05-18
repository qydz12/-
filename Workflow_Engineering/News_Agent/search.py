###搜索新闻
###此时已经不是普通搜索了，而是专门针对新闻的搜索，使用了Tavily这个工具
# from tavily import TavilyClient
# from dotenv import load_dotenv
# import os

# load_dotenv()

# client = TavilyClient(
#     api_key=os.getenv("TAVILY_API_KEY")
# )

# def search_news(topic):

#     response = client.search(
#         query=f"latest news about {topic}",
#         search_depth="advanced",
#         max_results=5
#     )

#     return response["results"]

###代码升级，增加了对新闻发布时间的过滤，确保只获取最近3天内的新闻，保证新闻的时效性和相关性。
###AI版
# from tavily import TavilyClient
# from dotenv import load_dotenv
# import os
# from datetime import datetime, timedelta

# load_dotenv()

# client = TavilyClient(
#     api_key=os.getenv("TAVILY_API_KEY")
# )

# def search_news(topic):

#     response = client.search(
#         query=f"latest news about {topic}",
#         search_depth="advanced",
#         max_results=10
#     )

#     results = response["results"]

#     filtered_news = []

#     now = datetime.utcnow()

#     for news in results:

#         published_date = news.get("published_date")

#         if published_date:

#             try:
#                 news_time = datetime.fromisoformat(
#                     published_date.replace("Z", "")
#                 )

#                 # 过滤3天前新闻
#                 if now - news_time <= timedelta(days=3):

#                     filtered_news.append(news)

#             except:
#                 continue

#     return filtered_news


###升级版
from tavily import TavilyClient
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def search_news(topic):

    response = client.search(
        query=f"latest news about {topic}",
        search_depth="advanced",
        max_results=8
    )

    results = response["results"]

    filtered_news = []

    now = datetime.utcnow()

    for news in results:

        published_date = news.get("published_date")

        # 如果没有时间
        # 先保留
        if not published_date:

            filtered_news.append(news)
            continue

        try:

            news_time = datetime.fromisoformat(
                published_date.replace("Z", "")
            )

            # 过滤3天前新闻
            if now - news_time <= timedelta(days=3):

                filtered_news.append(news)

        except:

            # 时间解析失败也保留
            filtered_news.append(news)

    return filtered_news