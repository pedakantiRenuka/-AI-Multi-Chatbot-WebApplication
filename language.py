import streamlit as st
import google.generativeai as gen_ai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini AI
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel("gemini-1.5-flash")

# Supported languages
LANGUAGES = {
    "Auto-Detect": "auto",
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Hindi": "hi",
    "Chinese": "zh",
    "Japanese": "ja",
    "Arabic": "ar",
}

# Detect Language Function
def detect_language(text):
    prompt = f"Detect the language of the following text and return only the name of the language:\n\nText: {text}"
    response = model.generate_content(prompt)
    return response.text.strip().replace('"', '').replace("Language:", "").strip()

# Translate Text Function
def translate_text(text, source, target):
    if source == "Auto-Detect":
        source_lang = detect_language(text)
        prompt = f"Translate the following text from {source_lang} to {target}:\n\nText:\n{text}\n\nReturn only the translated text."
    else:
        source_lang = source
        prompt = f"Translate the following text from {source} to {target}:\n\nText:\n{text}\n\nReturn only the translated text."

    response = model.generate_content(prompt)
    return source_lang, response.text.strip().strip('"') if response else None

# Streamlit App
def run():
    st.set_page_config(page_title="Language Detector & Translator", layout="centered")
    st.title("🌍 Language Detector & Translator")

    task = st.radio("Choose Task:", ["🔍 Detect Language", "🌐 Translate Text"], horizontal=True)
    text_input = st.text_area("📝 Enter your text here:", "", height=150)

    if task == "🔍 Detect Language":
        if st.button("Detect Language"):
            if not text_input.strip():
                st.warning("Please enter some text.")
                return
            detected_lang = detect_language(text_input)
            st.subheader("📌 Detected Language:")
            st.success(detected_lang)

    elif task == "🌐 Translate Text":
        col1, col2 = st.columns(2)
        with col1:
            source_language = st.selectbox("From (Source Language):", list(LANGUAGES.keys()))
        with col2:
            target_language = st.selectbox("To (Target Language):", list(LANGUAGES.keys()), index=4)

        if st.button("Translate"):
            if not text_input.strip():
                st.warning("Please enter some text.")
                return

            source_lang_display, translated = translate_text(text_input, source_language, target_language)

            if translated:
                st.markdown("### 🔄 Translation Result")
                col1, col2 = st.columns(2)

                with col1:
                    st.markdown(f"**Detected Source: {source_lang_display}**")
                    st.code(text_input, language="text")
                with col2:
                    st.markdown(f"**{target_language}:**")
                    st.code(translated, language="text")
            else:
                st.error("⚠️ Translation failed or no response from AI.")

# Run the app
if __name__ == "__main__":
    run()
