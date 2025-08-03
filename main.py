import streamlit as st
from streamlit_option_menu import option_menu
import emailspamdetection
import sentiment
import summarization
import grammar
import language

# Page Configuration
st.set_page_config(page_title="AI Multi-Chatbot", page_icon="🤖", layout="wide")

# Custom Sidebar Theme
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #D87093;
            padding: 20px;
            border-right: 2px solid #C71585;
            overflow: hidden;
        }
        [data-testid="stSidebarNav"] {
            color: #ffffff;
            font-size: 18px;
            font-weight: bold;
        }
        [data-testid="stSidebar"] a {
            color: #ffffff !important;
            font-size: 16px;
        }
        [data-testid="stSidebar"] a:hover {
            color: #FFB6C1 !important;
            font-weight: bold;
        }
        ::-webkit-scrollbar {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Menu
with st.sidebar:
    selected = option_menu(
        menu_title="🤖 AI Multi-Chatbot",
        options=[
            "📧 Email Classification",
            "🧠 Sentiment Analysis",
            "📝 Text Summarization",
            "🔤 Grammar Correction",
            "🌍 Language Translation"
        ],
        icons=[
            "envelope",
            "bar-chart",
            "file-text",
            "spellcheck",
            "translate"
        ]
    )

# Feature Routing
if selected == "📧 Email Classification":
    emailspamdetection.run()
elif selected == "🧠 Sentiment Analysis":
    sentiment.run()
elif selected == "📝 Text Summarization":
    summarization.run()
elif selected == "🔤 Grammar Correction":
    grammar.run()
elif selected == "🌍 Language Translation":
    language.run()



