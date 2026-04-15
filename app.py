import streamlit as st
import google.generativeai as genai
import json

# 1. SETUP
# We access the "Secret Safe" using st.secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-flash-latest')

# 2. WEBSITE TITLE
st.title("🤖 My AI Assistant")
st.write("Ask me anything, and I will generate a JSON Object for you.")

# 3. THE INPUT BOX (Replaces 'input()')
user_prompt = st.text_input("Type your prompt here:", placeholder="e.g., List 3 planets")

# 4. THE BUTTON
if st.button("Generate Answer"):
    if user_prompt:
        try:
            # Show a spinner while loading
            with st.spinner("Thinking..."):
                # Get response
                response = model.generate_content(
                    user_prompt,
                    generation_config={"response_mime_type": "application/json"}
                )
                
                # Convert to Python Object
                my_object = json.loads(response.text)

            # 5. DISPLAY RESULTS (Replaces 'print()')
            st.success("Success! Here is your data:")
            
            # Draw the JSON nicely
            st.json(my_object)
            
            # Show the proof message
            if isinstance(my_object, (dict, list)):
                st.info("✅ Tech Check: This is a valid Python/JSON Object.")
                
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please type something first!")