# =========================================
# Sidebar
# =========================================
import streamlit as st

def render_sidebar():
    with st.sidebar:

        st.title("🧠 AI Intelligence")

        topic = st.text_input(
            "新闻主题",
            placeholder="输入主题"
        )

        max_news = st.slider(
            "新闻数量",
            5,
            30,
            10
        )

        time_range = st.selectbox(
            "时间范围",
            [
                "24小时",
                "3天",
                "7天"
            ]
        )

        st.markdown("### 来源过滤")

        trusted_only = st.checkbox(
        "仅显示可信来源",
        value=False
    )
        st.markdown("### 分析模式")

        analysis_mode = st.radio(
            "分析模式",
            [
                "快速概览",
                "平衡分析",
                "深度情报"
            ],
            label_visibility="collapsed"
        )

        st.markdown("---")

        st.markdown("""
        ### 热门主题

        - AI
        - 金融
        - 国际局势
        - 游戏
        """)

        analyze_btn = st.button("开始分析")

        return {
        "topic": topic,
        "max_news": max_news,
        "time_range": time_range,
        "trusted_only": trusted_only,
        "analysis_mode": analysis_mode,
        "analyze_btn": analyze_btn
    }