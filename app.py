import streamlit as st
import requests

API_KEY = "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"  # 🔐 Replace with your OpenRouter API key

API_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def get_response_from_openrouter(user_message):
    body = {
        "model": "openai/gpt-3.5-turbo",  # ✅ Correct model ID
        "messages": [
            {"role": "system", "content": "You are a supportive mental health assistant who listens and gives calm, positive advice."},
            {"role": "user", "content": user_message}
        ]
    }

    res = requests.post(API_URL, headers=HEADERS, json=body)

    if res.status_code == 200:
        return res.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {res.status_code} — {res.text}"

# Streamlit UI
st.set_page_config(page_title="Mental Health Chatbot", page_icon="🧠")
st.title("🧠 Mental Health Chatbot")
st.write("This is a supportive chatbot for mental wellness. Start chatting below.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    st.session_state.chat_history.append(("You", user_input))
    with st.spinner("Bot is thinking..."):
        bot_reply = get_response_from_openrouter(user_input)
    st.session_state.chat_history.append(("Bot", bot_reply))

# Display chat history
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**You**: {message}")
    else:
        st.markdown(f"**Bot**: {message}")
