
import streamlit as st

st.header('fredom fighters')
name = st.radio(
    "what was your name last time we met:",
    ["athychew","mager cat","sofia","amilya","nicol","none of the above"],
    index=5)

if name == "none of the above":
    st.write("get lost ")
    st.image("getlost.jpeg")
else:
    st.write("welcome "+name)
    st.image("member.webp")


    topic = st.radio(
        "pike a topic :",
        ["fighting ","masc","wepon"],
        index=0)


A, col2, col3 = st.columns(3)