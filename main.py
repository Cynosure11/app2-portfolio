import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=300)
with col2:
    st.title("Aial Atlasov")
    content = """
    Hi, I am Aial! I am a Python programmer and founder of AI Sport Solution
    """
    st.info(content)
