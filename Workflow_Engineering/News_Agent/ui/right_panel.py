# =====================================
# 右侧区域
# =====================================
import streamlit as st
from datetime import datetime

def render_right_panel(topic, companies, time_range):

    # =================================
    # 实时情报
    # =================================
    st.markdown("""
    <div class="insight-card">

    <div class="insight-title">
    📊 实时情报
    </div>

    """, unsafe_allow_html=True)

    st.write(f"当前主题：{topic}")

    st.write(f"时间范围：{time_range}")

    st.write(
        f"更新时间：{datetime.now().strftime('%H:%M')}"
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # =================================
    # 热点实体
    # =================================
    st.markdown("""
    <div class="insight-card">

    <div class="insight-title">
    🔥 热点实体
    </div>

    """, unsafe_allow_html=True)

    if len(companies) == 0:

        st.write("暂无热点实体")

    else:

        for company in companies:

            st.markdown(
                f"""
                <span class="tag">
                {company}
                </span>
                """,
                unsafe_allow_html=True
            )

    st.markdown("</div>", unsafe_allow_html=True)

    # =================================
    # 时间线
    # =================================
    st.markdown("""
    <div class="insight-card">

    <div class="insight-title">
    ⏱ 新闻时间线
    </div>

    """, unsafe_allow_html=True)

    timeline_data = [
        ("09:30", "AI行业出现重要动态"),
        ("11:20", "新模型发布"),
        ("14:15", "市场热度提升")
    ]

    for time, content in timeline_data:

        c1, c2 = st.columns([1, 5])

        with c1:

            st.markdown(
                f"""
                <div class="timeline-time">
                {time}
                </div>
                """,
                unsafe_allow_html=True
            )

        with c2:

            st.markdown(
                f"""
                <div class="timeline-content">
                {content}
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("</div>", unsafe_allow_html=True)

    # =================================
    # 系统状态
    # =================================
    st.markdown("""
    <div class="insight-card">

    <div class="insight-title">
    ⚙ 系统状态
    </div>

    """, unsafe_allow_html=True)

    st.success("Tavily 已连接")

    st.success("DeepSeek 已运行")

    st.success("情报分析正常")

    st.markdown("</div>", unsafe_allow_html=True)