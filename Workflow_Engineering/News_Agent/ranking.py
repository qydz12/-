###新闻评分
###AI版
# from datetime import datetime

# def calculate_news_score(news):

#     score = 0

#     url = news.get("url", "").lower()

#     title = news.get("title", "").lower()

#     # 来源评分
#     if "reuters" in url:
#         score += 30

#     if "techcrunch" in url:
#         score += 20

#     if "openai" in url:
#         score += 25

#     # AI关键词
#     important_keywords = [
#         "gpt",
#         "agent",
#         "llm",
#         "deepseek",
#         "openai",
#         "anthropic"
#     ]

#     for keyword in important_keywords:

#         if keyword in title:
#             score += 10

#     # Tavily相关性
#     score += int(news.get("score", 0) * 10)

#     return score

###升级版
def calculate_news_score(news, topic):

    score = 0

    title = news.get("title", "").lower()

    content = news.get("content", "").lower()

    url = news.get("url", "").lower()

    # 主题关键词加分
    if topic.lower() in title:
        score += 20

    if topic.lower() in content:
        score += 10

    # 来源可信度
    trusted_sources = [
        "reuters",
        "bbc",
        "cnn",
        "apnews",
        "nytimes",
        "theguardian"
    ]

    for source in trusted_sources:

        if source in url:
            score += 15

    # Tavily原始相关性
    score += int(news.get("score", 0) * 10)

    return score