# =========================================
# 顶部
# =========================================
import streamlit as st

def render_header():
    st.markdown(
        '<div class="main-title">' \
        'AI 新闻情报中心'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">' \
        '实时新闻检索 · AI情报分析 · 趋势洞察'
        '</div>',
        unsafe_allow_html=True
    )