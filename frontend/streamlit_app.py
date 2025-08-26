import streamlit as st
import requests

st.title("Chatbot Demo")

# User input
user_input = st.text_input("Enter your message:")

if st.button("Send"):
    if user_input.strip():
        # Call FastAPI backend
        response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={"prompt": user_input}
        )

        if response.status_code == 200:
            st.write("🤖 Bot:", response.json()["answer"])
        else:
            st.error("Something went wrong with the API call.")
