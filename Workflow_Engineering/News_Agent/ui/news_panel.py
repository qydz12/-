# =================================
# 新闻流
# =================================
import streamlit as st

def render_news_panel(news_results):

    if len(news_results) == 0:
        st.warning("未搜索到相关新闻")
        return

    for news in news_results:

        title = news.get("title", "无标题")
        content = news.get("content", "暂无内容")
        url = news.get("url", "")
        published = news.get("published_date", "未知时间")

        st.markdown(f"""
        <div class="news-card">

            <div class="news-title">
            {title}
            </div>

            <div class="news-meta">
            发布时间：{published}
            </div>

            <div class="news-content">
            {content}
            </div>

        </div>
        """, unsafe_allow_html=True)

        if url:
            st.link_button("查看原文", url)