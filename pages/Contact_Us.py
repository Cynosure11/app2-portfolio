from pydoc_data.topics import topics

import streamlit as st
from send_email import send_email
import pandas as pd

df = pd.read_csv("topics.csv")

st.header("Contact Us")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    option = st.selectbox(
        "What topic do you want to discuss?",
        df["topic"]
    )
    raw_message = st.text_area("Text")
    message = f"""\
Subject: New email from {user_email}

From: {user_email} 
Topic: {option}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        send_email(message)
        st.info("Your email was sent successfully")


