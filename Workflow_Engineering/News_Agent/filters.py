###过滤低质量新闻
TRUSTED_SOURCES = [

    # 国际新闻
    "reuters.com",
    "apnews.com",
    "bbc.com",
    "cnn.com",
    "nytimes.com",
    "theguardian.com",

    # 科技AI
    "techcrunch.com",
    "theverge.com",
    "openai.com",
    "deepseek.com",
    "huggingface.co",

    # 技术媒体
    "wired.com",
    "arstechnica.com",

    # 开发技术
    "github.com"
]
def filter_by_source(news_list):

    filtered = []

    for news in news_list:

        url = news.get("url", "")

        for source in TRUSTED_SOURCES:

            if source in url:

                filtered.append(news)
                break

    return filtered

def deduplicate_news(news_list):

    seen_titles = set()

    unique_news = []

    for news in news_list:

        title = news.get("title", "").strip()

        if title not in seen_titles:

            seen_titles.add(title)

            unique_news.append(news)

    return unique_news