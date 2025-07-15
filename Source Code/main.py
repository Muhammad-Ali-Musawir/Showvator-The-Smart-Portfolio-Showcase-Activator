import os
import streamlit as st
import requests

# Load API key
API_KEY = st.secrets["OPENROUTER_API_KEY"]

# Load portfolio text
with open("Assets/portfolio.txt", "r", encoding="utf-8") as file:
    portfolio = file.read()

# Set page config
st.set_page_config(
    page_title="Showvator – Portfolio Chatbot",
    page_icon="Assets/icon.ico",
    layout="wide"
)

# Apply some custom CSS for styling
st.markdown("""
    <style>
        .stChatMessage {
            padding: 10px 16px;
            border-radius: 12px;
            margin-bottom: 10px;
        }
        .user-message {
            background-color: #DCF8C6;
            text-align: right;
        }
        .assistant-message {
            background-color: #F1F0F0;
            text-align: left;
        }
        .message-container {
            border-radius: 15px;
            padding: 10px;
            margin-bottom: 12px;
        }
        .stApp {
            background-color: #FAFAFA;
        }
    </style>
""", unsafe_allow_html=True)

# Header section
col1, col2 = st.columns([0.1, 0.9])
with col1:
    st.image("Assets/logo.png", width=72)
with col2:
    st.markdown("## 👨‍💼 Showvator – Portfolio Chatbot")
    st.caption("Get to know Muhammad Ali Musawir – Ask anything!")

st.divider()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": f"""
You are Muhammad Ali Musawir — a confident, intelligent, and friendly engineer. You are answering questions about your work, skills, achievements, and background — as if you're speaking directly to the person.

❗ Do NOT mention you're an AI, assistant, or chatbot. Do not say anything about 'portfolio', 'document', or 'source'. Speak naturally, clearly, and professionally — as if it's truly you.

🎯 Your goal is to **impress the user with your personality and way of talking**. Be articulate, expressive, and warm — but stay humble and focused. Use emojis where it feels appropriate.

Here is your background and achievements:

{portfolio}
"""
        }
    ]

# Chat input
user_input = st.chat_input("Ask anything about Muhammad Ali Musawir...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # OpenRouter API call
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek/deepseek-chat-v3-0324:free",
        "messages": st.session_state.messages
    }
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        st.session_state.messages.append({"role": "assistant", "content": reply})
    else:
        st.session_state.messages.append({"role": "assistant", "content": "⚠️ Error getting response."})

# Display chat history
for msg in st.session_state.messages[1:]:
    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        st.markdown(msg["content"])
