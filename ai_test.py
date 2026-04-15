import google.generativeai as genai
import json

# 1. SETUP
# Paste your key inside the quotes below
genai.configure(api_key="AIzaSyDGlzUWdOJVcTSzaq_HZREVMCVB_35vJGI")

# 2. MODEL
model = genai.GenerativeModel('gemini-flash-latest')

# 3. ASK
user_prompt = input("Enter a prompt (e.g., 'List 3 fruits'): ")

# 4. GET THE ANSWER (As text)
response = model.generate_content(
    user_prompt,
    generation_config={"response_mime_type": "application/json"}
)

# 5. THE CONVERSION (This is the specific step your mentor wants)
# We take the text string and convert it into a real Python Dictionary
my_object = json.loads(response.text)

# 6. PROOF OF SUCCESS
print("\n--- 1. Raw JSON String (The Box) ---")
print(response.text)

print("\n--- 2. Python Object (The Content) ---")
print(my_object)

# This line proves it is an object, not just text
if isinstance(my_object, (dict, list)):
    print("\n[SUCCESS] Great job! This is technically a Python Object.")