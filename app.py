import streamlit as st

st.title("我的第一个AI网页")

name = st.text_input("请输入名字")

if st.button("提交"):

    st.write(f"你好，{name}")