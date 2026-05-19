import streamlit as st
from agent import run_news_agent
from ui.styles import load_css
from ui.sidebar import render_sidebar
from ui.header import render_header
from ui.metrics import render_metrics
from ui.analysis_panel import render_analysis
from ui.news_panel import render_news_panel
from ui.right_panel import render_right_panel

load_css()
# =========================================
# 页面配置
# =========================================
st.set_page_config(
    page_title="AI Intelligence Hub",
    page_icon="🧠",
    layout="wide"
)
load_css()



config = render_sidebar()
render_header()

topic = config["topic"]

max_news = config["max_news"]

trusted_only = config["trusted_only"]

analysis_mode = config["analysis_mode"]

analyze_btn = config["analyze_btn"]

time_range = config["time_range"]



# =========================================
# 主逻辑
# =========================================
if analyze_btn:

    if not topic:

        st.warning("请输入新闻主题")

    else:

        # =====================================
        # 进度
        # =====================================
        progress_placeholder = st.empty()

        status_placeholder = st.empty()

        progress = progress_placeholder.progress(0)

        status_placeholder.info("正在连接新闻搜索引擎...")

        progress.progress(20)

        status_placeholder.info("正在抓取最新新闻...")

        progress.progress(40)

        status_placeholder.info("正在过滤低可信内容...")

        progress.progress(60)

        status_placeholder.info("正在进行AI分析...")

        progress.progress(80)

        # =====================================
        # Agent
        # =====================================
        result = run_news_agent(
            topic
        )

        progress.progress(100)

        progress_placeholder.empty()

        status_placeholder.empty()

        # =====================================
        # 数据
        # =====================================
        news_results = result["news"]

        # =====================================
        # 来源可信度过滤
        # =====================================

        trusted_domains = [

            "reuters.com",
            "bbc.com",
            "bloomberg.com",
            "cnn.com",
            "nytimes.com",
            "forbes.com",
            "techcrunch.com",
            "theverge.com",
            "wired.com"
        ]

        filtered_news = []
        trusted_news = []
        # 开启可信来源过滤
        if trusted_only:

            for news in news_results:

                url = news.get(
                    "url",
                    ""
                ).lower()

                for domain in trusted_domains:

                    if domain in url:

                        filtered_news.append(news)
                        trusted_news.append(news)
                        break

        # 未开启过滤
        else:

            filtered_news = news_results

            # 计算所有新闻中的可信来源数量
            for news in news_results:

                url = news.get(
                    "url",
                    ""
                ).lower()

                for domain in trusted_domains:

                    if domain in url:

                        trusted_news.append(news)
                        break

        # =====================================
        # 防止过滤后为空
        # =====================================

        if len(filtered_news) == 0:

            filtered_news = news_results

        # =====================================
        # 热点实体提取
        # =====================================
        companies = []

        keywords = [
            "OpenAI",
            "微软",
            "谷歌",
            "Meta",
            "英伟达",
            "DeepSeek",
            "腾讯",
            "阿里"
        ]

        for news in filtered_news:

            text = (
                news.get("title", "") +
                news.get("content", "")
            )

            for k in keywords:

                if k in text and k not in companies:

                    companies.append(k)

        # =====================================
        # 主布局
        # =====================================
        left, center, right = st.columns([
            0.2,
            2.3,
            1
        ])

        # =====================================
        # 中间区域
        # =====================================
        with center:
            
            render_metrics(
                len(filtered_news),
                len(trusted_news),
                analysis_mode
            )

            st.markdown("<br>", unsafe_allow_html=True)

            # =================================
            # Tabs
            # =================================


            tab1, tab2 = st.tabs([
                "🧠 AI情报分析",
                "📰 新闻流"
            ])

            with tab1:
                render_analysis(result)

            with tab2:
                render_news_panel(filtered_news)

        with right:
            render_right_panel(
                topic,
                companies,
                time_range
            )