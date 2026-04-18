# 🤖 My AI Assistant

A lightweight and modern **Streamlit AI Assistant** powered by **OpenRouter API**.  
Enter any prompt, choose a model, and receive natural language responses instantly.

---

## ✨ Features

- 🎨 Clean and responsive Streamlit interface  
- 🤖 Connects to OpenRouter models  
- 💬 Returns human-like text answers (not raw JSON)  
- 🔐 Secure API key handling with `secrets.toml`  
- ⚡ Fast and simple setup  
- 🧠 Easily switch models anytime

---

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **OpenAI Python SDK**
- **OpenRouter API**

---

## 🚀 How It Works

1. Reads your API key from Streamlit secrets.
2. Sends your prompt to the selected OpenRouter model.
3. Displays the AI-generated response directly in the browser.

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/my-ai-assistant.git
cd my-ai-assistant

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
secrets.toml
OPENROUTER_API_KEY = "your_openrouter_api_key"
OPENROUTER_MODEL = "google/gemma-4-31b-it:free"
OPENROUTER_HTTP_REFERER = "http://localhost:8501"
OPENROUTER_APP_TITLE = "My AI Assistant"
streamlit run app.py
```
💡 Usage
Open the Streamlit app in your browser
Type your prompt into the input box
Click Generate Answer
Wait for the AI response

📁 Project Structure
my-ai-assistant/
│── app.py                 # Main Streamlit application
│── requirements.txt       # Python dependencies
│── .streamlit/
│   └── secrets.toml       # Local secrets (not pushed to GitHub)
│── .gitignore             # Ignores venv + secrets
│── README.md

🧪 Example
Prompt
What are three benefits of using Streamlit?

Response
1. Fast web app development
2. Easy Python integration
3. Great for ML and AI projects

⚠️ Notes
Never commit your API key to GitHub.
If you get a 404 error, verify the model name in secrets.toml.
Recommended free model:
google/gemma-4-31b-it:free

🌟 Future Improvements
Chat history
Dark mode UI
Multiple model selection
File upload support
Voice input/output

📜 License

MIT License
