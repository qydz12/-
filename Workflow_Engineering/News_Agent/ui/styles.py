# =========================================
# CSS
# =========================================
import streamlit as st
def load_css():
    st.markdown("""
    <style>

    /* ======================================
    整体页面
    ====================================== */
    .stApp {
        background-color: #0B1220;
        color: white;
    }

    .block-container {
        padding-top: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    /* ======================================
    Sidebar
    ====================================== */
    section[data-testid="stSidebar"] {
        background-color: #111827;
        border-right: 1px solid #1F2937;
    }

    /* ======================================
    标题
    ====================================== */
    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: white;
        margin-bottom: 10px;
    }

    .main-subtitle {
        font-size: 17px;
        color: #94A3B8;
        margin-bottom: 30px;
    }

    /* ======================================
    统一卡片
    ====================================== */
    .card {
        background: #111827;
        border: 1px solid #1F2937;
        border-radius: 18px;
        padding: 24px;
        margin-bottom: 20px;
    }

    /* ======================================
    指标卡
    ====================================== */
    .metric-card {
        background: #111827;
        border: 1px solid #1F2937;
        border-radius: 16px;
        padding: 22px;
    }

    .metric-value {
        font-size: 38px;
        font-weight: 800;
        color: white;
    }

    .metric-label {
        color: #94A3B8;
        font-size: 14px;
        margin-top: 5px;
    }
                
    /* ======================================
    Streamlit Metric组件
    ====================================== */

    [data-testid="stMetric"] {

        background: #111827;
        border: 1px solid #1F2937;
        padding: 20px;
        border-radius: 18px;
    }

    [data-testid="stMetricLabel"] {

        color: #94A3B8;
        font-size: 14px;
    }

    [data-testid="stMetricValue"] {

        color: white;
        font-size: 38px;
        font-weight: 800;
    }

    /* ======================================
    Section标题
    ====================================== */
    .section-title {
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 18px;
        color: white;
    }

    /* ======================================
    新闻卡片
    ====================================== */
    .news-card {
        background: #111827;
        border: 1px solid #1F2937;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 18px;
    }

    .news-title {
        font-size: 20px;
        font-weight: 700;
        color: white;
        margin-bottom: 12px;
    }

    .news-meta {
        color: #94A3B8;
        font-size: 13px;
        margin-bottom: 15px;
    }

    .news-content {
        color: #D1D5DB;
        line-height: 1.9;
        font-size: 15px;
    }

    /* ======================================
    标签
    ====================================== */
    .tag {
        display: inline-block;
        background-color: #1E3A8A;
        color: white;
        padding: 6px 14px;
        border-radius: 999px;
        margin-right: 8px;
        margin-bottom: 8px;
        font-size: 12px;
    }

    /* ======================================
    输入框
    ====================================== */
    .stTextInput input {
        background-color: #1F2937 !important;
        color: white !important;
        border: 1px solid #374151 !important;
        border-radius: 10px !important;
    }

    /* ======================================
    下拉框
    ====================================== */
    div[data-baseweb="select"] > div {
        background-color: #1F2937 !important;
        color: white !important;
        border: 1px solid #374151 !important;
    }

    /* ======================================
    Slider
    ====================================== */
    .stSlider {
        color: white;
    }

    /* ======================================
    按钮
    ====================================== */
    .stButton button {
        width: 100%;
        height: 50px;
        background-color: #2563EB;
        color: white;
        border: none;
        border-radius: 12px;
        font-size: 16px;
        font-weight: 700;
    }

    .stButton button:hover {
        background-color: #1D4ED8;
    }

    /* ======================================
    Checkbox / Radio
    ====================================== */
    .stCheckbox label {
        color: #D1D5DB !important;
    }

    .stRadio label {
        color: #D1D5DB !important;
    }

    /* ======================================
    右侧情报卡
    ====================================== */
    .insight-card {
        background: #111827;
        border: 1px solid #1F2937;
        border-radius: 16px;
        padding: 18px;
        margin-bottom: 18px;
    }

    .insight-title {
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 15px;
    }

    /* ======================================
    时间线
    ====================================== */
    .timeline-time {
        color: #60A5FA;
        font-size: 13px;
    }

    .timeline-content {
        color: white;
        padding-bottom: 15px;
        border-left: 2px solid #2563EB;
        padding-left: 15px;
    }

    /* ======================================
    Tabs
    ====================================== */
    .stTabs [data-baseweb="tab"] {
        color: #94A3B8;
    }

    </style>
    """, unsafe_allow_html=True)