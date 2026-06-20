import streamlit as st

from app.chatbot import get_answer

st.set_page_config(
    page_title="Persona Adaptive Support Agent"
)

st.title("🤖 Persona Adaptive Support Agent")

query = st.text_input(
    "Ask a customer support question"
)

if st.button("Ask"):

    if query:

        answer = get_answer(query)

        st.success(answer)