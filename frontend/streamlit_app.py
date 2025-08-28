import streamlit as st
import requests
import os

st.title("Chatbot Demo")

# Detect backend URL (Render or Local)
BACKEND_URL = os.getenv("BACKEND_URL", "https://streamliteproj.onrender.com")

st.write(f"🔗 Using backend: {BACKEND_URL}")

# ✅ Initialize session state messages if not already there
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input.strip():
        # Save user message
        st.session_state.messages.append({"role": "user", "content": user_input})

        try:
            response = requests.post(
                f"{BACKEND_URL}/chat",   # ✅ Correct endpoint
                json={
                    "prompt": user_input,     # ✅ must be prompt not message
                    "persona": "Default",     # ✅ backend expects this
                    "history": st.session_state.messages  # ✅ chat history
                }
            )

            if response.status_code == 200:
                data = response.json()
                bot_reply = data.get("answer") or str(data)

                # Save bot reply
                st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            else:
                st.session_state.messages.append(
                    {"role": "bot", "content": f"⚠️ API error: {response.status_code} | {response.text}"}
                )
        except Exception as e:
            st.session_state.messages.append({"role": "bot", "content": f"🚨 {e}"})

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"🧑 **You:** {msg['content']}")
    else:
        st.markdown(f"🤖 **Bot:** {msg['content']}")
