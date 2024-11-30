import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=300)
with col2:
    st.title("Aial Atlasov")
    content = """
    Hi, I am Aial! I am a Python programmer and founder of AI Sport Solution.
    I graduated in 2024 with a Bachelor degree of Engineering in North Eastern Federal
    University with a focus on using Python for remote sensing. I have worked with 
    companies from various countries, such as the Center for Conversation Geography,
    to map and understand Siberian ecosystems, image processing with the Swiss in-Terra, 
    and performing data mining to gain business insights with the Siberian Rapid intelligence.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel Free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df=  pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
