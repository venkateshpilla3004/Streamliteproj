import streamlit as st
import requests
import os

st.title("Chatbot Demo")

# Detect backend URL (Render or Local)
BACKEND_URL = os.getenv("BACKEND_URL", "https://streamliteproj.onrender.com/chat")

st.write(f"🔗 Using backend: {BACKEND_URL}")

# User input
user_input = st.text_input("Enter your message:")

if st.button("Send"):
    if user_input.strip():
        try:
            response = requests.post(
                BACKEND_URL,
                json={"prompt": user_input}
            )

            if response.status_code == 200:
                st.write("🤖 Bot:", response.json()["answer"])
            else:
                st.error(f"⚠️ API error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"🚨 Failed to connect to backend: {e}")
