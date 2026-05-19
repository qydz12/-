# =================================
# 指标
# =================================
import streamlit as st


def render_metrics(news_count: int, trusted_count: int, mode: str):
    """渲染顶部指标卡片

    参数:
        news_count: 新闻总数
        trusted_count: 可信来源数量
        mode: 分析模式名称
    """
    trusted_pct = round(trusted_count / news_count * 100, 1) if news_count > 0 else 0.0

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric(
            label="📰 新闻数量",
            value=news_count
        )

    with m2:
        st.metric(
            label="✅ 可信来源",
            value=trusted_count,
            delta=f"{trusted_pct}% 占比"
        )

    with m3:
        # 模式对应的 emoji
        mode_icon = {"快速概览": "⚡", "平衡分析": "⚖️", "深度情报": "🔍"}
        icon = mode_icon.get(mode, "🧠")

        st.metric(
            label="🎯 分析模式",
            value=f"{icon} {mode}"
        )

    st.markdown("<br>", unsafe_allow_html=True)
