# 🧠 AI Multi-Chatbot Web Application

An interactive multi-feature AI chatbot built with **Streamlit**, integrating five powerful Natural Language Processing (NLP) tools:  
📧 Email Spam Detection • 😊 Sentiment Analysis • ✍️ Grammar Correction • 🧾 Text Summarization • 🌍 Language Translation

---

## 🚀 Features

- **Email Spam Detection**: Classifies emails as 'Spam' or 'Not Spam' using ML techniques.
- **Sentiment Analysis**: Determines sentiment polarity (Positive, Negative, Neutral).
- **Text Summarization**: Generates concise summaries from long text using Google Gemini API.
- **Grammar Correction**: Identifies and corrects grammatical errors.
- **Language Translation**: Detects language and translates text between multiple languages.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **NLP/AI**: Google Gemini API
- **Environment Management**: `python-dotenv`
- **Language Detection**: `langdetect`

---

## 📁 Project Structure

AI-Multi-Chatbot-WebApplication/
├── main.py # Streamlit app with sidebar UI
├── emailspamdetection.py # Spam detection logic
├── sentiment.py # Sentiment analysis logic
├── summarization.py # Text summarization using Gemini
├── grammar.py # Grammar correction using Gemini
├── language.py # Language detection and translation
├── requirements.txt # Project dependencies
└── .env.example # Example for setting up environment variables


3. Install Dependencies
  pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the root directory and add your Gemini API key:
GOOGLE_API_KEY=your_google_gemini_api_key

▶️ Run the App
streamlit run main.py

