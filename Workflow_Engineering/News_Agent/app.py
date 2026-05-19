import streamlit as st
###CSS样式
st.markdown(
    """
    <style>

    .main {
        background-color: #0E1117;
    }

    </style>
    """,
    unsafe_allow_html=True
)

from agent import run_news_agent

st.title("AI 新闻情报分析系统")

with st.sidebar:

    st.title("新闻Agent")

    topic = st.text_input(
        "请输入新闻主题"
    )

    max_news = st.slider(
        "新闻数量",
        5,
        20,
        10
    )

# if st.button("开始分析"):

#     col1, col2 = st.columns(2)

#     with col1:

#         st.metric(
#             "新闻数量",
#             len(news_results)
#         )

#     with col2:

#         st.metric(
#             "可信来源",
#             5
#         )

#     with st.spinner("正在分析最新新闻..."):

#         result = run_news_agent(topic)

#         analysis = result["analysis"]

#         news_results = result["news"]

#     tab1, tab2 = st.tabs([
#     "AI分析",
#     "原始新闻"
#     ])

#     with tab1:

#         st.markdown(analysis)

#     with tab2:

#         for news in news_results:

#             with st.container():

#                 st.subheader(
#                     news.get("title", "无标题")
#                 )

#                 st.write(
#                     news.get("content", "")
#                 )

#                 if news.get("url"):

#                     st.link_button(
#                         "查看原文",
#                         news["url"]
#                     )

#                 st.divider()

if st.button("开始分析"):

    with st.spinner("正在分析最新新闻..."):

        result = run_news_agent(topic)

        analysis = result["analysis"]

        news_results = result["news"]

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "新闻数量",
            len(news_results)
        )

    with col2:

        st.metric(
            "可信来源",
            5
        )

    tab1, tab2 = st.tabs([
        "AI分析",
        "原始新闻"
    ])

    with tab1:

        st.markdown(analysis)

    with tab2:

        for news in news_results:

            with st.container():

                st.subheader(
                    news.get("title", "无标题")
                )

                st.write(
                    news.get("content", "")
                )

                if news.get("url"):

                    st.link_button(
                        "查看原文",
                        news["url"]
                    )

                st.divider()