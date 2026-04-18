My AI Assistant
A simple Streamlit app that sends prompts to OpenRouter and returns normal text answers using a selected model.

Features
Clean Streamlit UI
OpenRouter integration
Simple text answers, not JSON
Model configured through Streamlit secrets
Safe local secret handling with secrets.toml
Tech Stack
Python
Streamlit
OpenAI Python SDK
OpenRouter API
How It Works
The app reads your OpenRouter API key from Streamlit secrets, sends your prompt to the selected model, and displays the response in the browser.

Setup
Create and activate a virtual environment.

python -m venv .venv
.venv\Scripts\activate

Install dependencies.

pip install -r requirements.txt

Create a .streamlit folder and add secrets.toml inside it.

OPENROUTER_API_KEY = "your_openrouter_api_key"
OPENROUTER_MODEL = "google/gemma-4-31b-it:free"

Optional:

OPENROUTER_HTTP_REFERER = "http://localhost:8501"
OPENROUTER_APP_TITLE = "My AI Assistant"

Run the app.

streamlit run app.py

Usage
Type a prompt in the text box.
Click Generate Answer.
Wait for the model response to appear on the page.
Project Structure
app.py - Main Streamlit app
requirements.txt - Python dependencies
secrets.toml - Local secrets file, not committed to GitHub
.gitignore - Ignores virtual environment and secrets
Example
Prompt:

What are three benefits of using Streamlit?

Response:

The app will show a natural language answer from the model.

Notes
Do not commit your API key.
If you get a 404 error, make sure the model slug in secrets.toml is valid on OpenRouter.
Recommended free model for this app:
google/gemma-4-31b-it:free
