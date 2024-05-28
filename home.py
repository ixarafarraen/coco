
import streamlit as st

st.header('fredom fighters')
name = st.radio(
    "what was your name last time we met:",
    ["athychew","mager cat","sofia","amilya","nicol","none of the above"])

if name == "none of the above":
    st.write("get lost ")
    st.image("getlost.jpeg")
else:
    st.write("welcome "+name)






A, col2, col3 = st.columns(3)