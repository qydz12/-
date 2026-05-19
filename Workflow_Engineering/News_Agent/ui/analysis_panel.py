# =================================
# AI分析
# =================================
# import streamlit as st

# def render_analysis(analysis_result):
#     st.markdown("""
#     <div class="section-title">
#     今日核心情报
#     </div>
#     """, unsafe_allow_html=True)

#     sections = analysis_result["analysis"].split("\n\n")

#     for section in sections:

#         if len(section.strip()) > 0:

#             with st.container():

#                 st.markdown("""
#                 <div class="card">
#                 """, unsafe_allow_html=True)

#                 st.markdown(
#                     f"""
#                     <div style="
#                     border-left:4px solid #3B82F6;
#                     padding-left:15px;
#                     line-height:1.9;
#                     font-size:15px;
#                     color:#D1D5DB;
#                     ">
#                     """,
#                     unsafe_allow_html=True
#                 )

#                 # 关键修复
#                 st.write(section)

#                 st.markdown("""
#                     </div>
#                 """, unsafe_allow_html=True)

#                 st.markdown("""
#                 </div>
#                 """, unsafe_allow_html=True)

import streamlit as st

def render_analysis(analysis_result):

    st.markdown("""
    <div class="section-title">
    今日核心情报
    </div>
    """, unsafe_allow_html=True)

    sections = analysis_result["analysis"].split("\n\n")

    for section in sections:
        if section.strip():

            with st.container():

                st.markdown("""<div class="card">""", unsafe_allow_html=True)

                st.markdown("""
                <div style="
                border-left:4px solid #3B82F6;
                padding-left:15px;
                line-height:1.9;
                font-size:15px;
                color:#D1D5DB;
                ">
                """, unsafe_allow_html=True)

                st.write(section)

                st.markdown("</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
