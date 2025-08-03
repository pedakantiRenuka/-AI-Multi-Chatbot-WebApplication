import streamlit as st
import google.generativeai as gen_ai
from dotenv import load_dotenv
import os
import re
import json

def run():
    # Load environment variables
    load_dotenv()
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    # Configure Gemini
    gen_ai.configure(api_key=GOOGLE_API_KEY)
    model = gen_ai.GenerativeModel('gemini-1.5-flash')

    st.title("📧 Email-Spam Detection")

    # Initialize history in session state
    if 'history' not in st.session_state:
        st.session_state.history = []

    # Spam detection prompt
    prompt = '''
    You are an AI-powered email spam detector. Your task is to analyze the given email content and classify it as either "Spam" or "Not Spam (Ham)".

    ### **Guidelines**:
    1. **Spam Identification**: If the email contains promotional offers, phishing attempts, scams, or excessive use of spam trigger words (e.g., "free", "win", "urgent", "claim now"), classify it as **Spam**.
    2. **Not Spam (Ham) Identification**: If the email is a regular, professional, or personal message without spam characteristics, classify it as **Not Spam**.
    3. **Strict Output Format**: Return the result in **valid JSON format only**, with no additional text. Example:

    ```json
    {"email_type": "Spam"}
    ```

    Ensure the response is valid JSON with no extra text.
    '''

    email_text = st.text_area("Enter the email content:", "")

    col1, col2 = st.columns([1, 1])

    with col1:
        detect = st.button("Detect Spam or Ham")
    with col2:
        clear = st.button("🗑️ Clear History")

    if detect:
        if email_text.strip() == "":
            st.warning("Please enter some text.")
        else:
            full_prompt = f'{prompt}\n\nEmail Content:\n"{email_text}"\n\nReturn JSON output:'
            response = model.generate_content(full_prompt)

            if response and response.text:
                raw_response = response.text.strip()

                match = re.search(r'\{.*\}', raw_response, re.DOTALL)
                if match:
                    json_content = match.group(0)
                    try:
                        email_classifier = json.loads(json_content)
                        email_type = email_classifier.get("email_type", "Unknown")
                        emoji = "🟥" if "spam" in email_type.lower() else "🟩"

                        st.markdown(f"🔍 **Email Type:** {emoji} {email_type}")

                        # Save to history
                        st.session_state.history.append({
                            "Email": email_text.strip(),
                            "Type": email_type
                        })

                    except json.JSONDecodeError:
                        st.error("Failed to parse response as JSON.")
                        st.write(raw_response)
                else:
                    st.error("No valid JSON found in the response.")
                    st.write(raw_response)

    if clear:
        st.session_state.history = []
        st.success("🧹 Detection history cleared.")

    if st.session_state.history:
        st.markdown("### 📜 Detection History")
        st.dataframe(st.session_state.history, use_container_width=True)

# Run app
if __name__ == "__main__":
    run()
