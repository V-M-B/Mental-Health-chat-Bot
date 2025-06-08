# 🧠 Mental Health Chatbot

A simple and supportive chatbot for mental wellness, built with **Python**, **Streamlit**, and the **OpenRouter API** (using GPT-3.5 Turbo or other open models).

This app creates a safe, local interface for users to talk about their feelings, receive calming responses, and engage in non-judgmental conversations for mental support.

---

## 🌟 Features

- 🧘 Mental health–focused chat support
- 💬 Real-time responses using GPT-3.5 Turbo (via OpenRouter)
- 🧠 Empathetic, non-judgmental tone
- 🖥️ Streamlit frontend – lightweight and easy to run locally

---

## 🔧 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io)
- **API**: [OpenRouter.ai](https://openrouter.ai) (Chat Completion Endpoint)
- **Language Model**: `openai/gpt-3.5-turbo` or any other supported model on OpenRouter

---

## 🚀 Getting Started

### 1. Clone the Repository or Download the Files

```bash
git clone https://github.com/your-username/mental-health-chatbot.git
cd mental-health-chatbot
2. Install Python Dependencies
Make sure Python 3.8+ is installed.

bash
Copy code
pip install streamlit requests
3. Get Your OpenRouter API Key
Go to: https://openrouter.ai/keys

Copy your API key (starts with sk-or-...)

Replace it in app.py:

python
Copy code
API_KEY = "sk-or-your_api_key_here"
4. Run the App
bash
Copy code
streamlit run app.py
It will open in your browser at http://localhost:8501.

✅ Available Models
In app.py, change the model name to switch engines:

python
Copy code
"model": "openai/gpt-3.5-turbo"
Other available models:

Model ID	Description
openai/gpt-3.5-turbo	Balanced, fast, great for chat
mistralai/mistral-7b-instruct	Open-source, lightweight
google/gemini-pro	Gemini LLM by Google
anthropic/claude-3-haiku	Claude 3's fastest model

Find the full list here: https://openrouter.ai/docs#models

🛡️ Privacy & Disclaimer
This tool is not a replacement for professional mental health care.

Conversations are not stored locally, but may be logged by model providers (via OpenRouter).

Do not share sensitive, private, or emergency-related information.

📂 Project Structure
bash
Copy code
mental-health-chatbot/
├── app.py         # Main Streamlit chatbot app
└── README.md      # This file
🧠 Ideas for Future Additions
📝 Journaling or gratitude prompts

🌤️ Mood tracking

📊 Sentiment analysis

☁️ Streamlit Cloud deployment

📜 License
This project is open-source under the MIT License.

🙋‍♂️ Author
Built by Varun M Bharadwaj
Guided by AI (ChatGPT 😄)
GitHub: github.com/your-github (Update your link here)