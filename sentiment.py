# import streamlit as st
# import google.generativeai as gen_ai
# from dotenv import load_dotenv
# import os
# import json

# # Load environment variables
# load_dotenv()
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# # Configure Gemini AI
# gen_ai.configure(api_key=GOOGLE_API_KEY)
# model = gen_ai.GenerativeModel("gemini-pro")

# # Function to analyze sentiment
# def analyze_sentiment(review_type, review_text):
#     sentiment_prompt = f"""
#     You are an AI that analyzes sentiment in {review_type.lower()}.
#     Classify the sentiment as **Positive**, **Neutral**, or **Negative** based on the review provided.

#     **Review:**
#     {review_text}

#     **Response Format (Strict JSON):**
#     {{
#         "sentiment": "Positive"   # or "Neutral" or "Negative"
#     }}
#     """

#     try:
#         response = model.generate_content(sentiment_prompt)
#         return json.loads(response.text) if response else {"sentiment": "Error: No response generated."}
#     except Exception as e:
#         return {"sentiment": f"Error: {e}"}

# # Function to run the Streamlit app
# def run():
#     """Runs the Sentiment Analysis app."""
#     st.title("🎭🍽 Sentiment Analysis for Food and Film Reviews")
#     st.write("Analyze Film or Food Reviews to determine their sentiment (Positive, Neutral, Negative).")

#     # Select type of review
#     review_type = st.radio("Choose Review Type:", ["🎬 Film Review", "🍔 Food Review"])

#     # User input
#     review_text = st.text_area("Enter the review text:", "", height=200)

#     if st.button("Analyze Sentiment"):
#         if review_text.strip() == "":
#             st.warning("Please enter a review.")
#         else:
#             sentiment_result = analyze_sentiment(review_type, review_text)

#             # Display sentiment result in JSON format
#             st.subheader("📌 Sentiment Analysis Result (JSON):")
#             st.json(sentiment_result)

# # Run the app when executed directly
# if __name__ == "__main__":
#     run()

import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Function to detect review type
def detect_review_type(review):
    prompt = f"""Classify the following review as either 'food' or 'film'. Reply ONLY with one word: 'food' or 'film'. 
Review: {review}"""
    try:
        response = model.generate_content(prompt)
        review_type = response.text.strip().lower()
        if "food" in review_type:
            return "food"
        elif "film" in review_type:
            return "film"
        else:
            return "unknown"
    except Exception as e:
        return "unknown"

# Function to analyze sentiment
def analyze_sentiment(review):
    prompt = f"""Analyze the sentiment of the following review. Reply with one of these: Positive, Neutral, Negative.
Review: {review}"""
    try:
        response = model.generate_content(prompt)
        sentiment = response.text.strip().lower()
        if "positive" in sentiment:
            return "Positive"
        elif "neutral" in sentiment:
            return "Neutral"
        elif "negative" in sentiment:
            return "Negative"
        else:
            return "Unclear"
    except Exception as e:
        return "Error"

# Run the Streamlit app
def run():
    st.title("🎭🍽 Sentiment Analysis for Food and Film Reviews")
    st.write("Analyze Film or Food Reviews to determine their sentiment (Positive, Neutral, Negative).")

    review_type_input = st.radio("Choose Review Type:", ["🎬 Film Review", "🍔 Food Review"])
    review = st.text_area("Enter the review text:")

    if st.button("Analyze"):
        if not review.strip():
            st.warning("Please enter a review text.")
        else:
            user_type = "film" if "film" in review_type_input.lower() else "food"
            detected_type = detect_review_type(review)
            sentiment = analyze_sentiment(review)

            if detected_type != "unknown" and detected_type != user_type:
                st.error(f"⚠️ The entered review seems to be about **{detected_type}**, but you selected **{user_type}**. Please check!")

            if sentiment == "Positive":
                st.success("✅ Sentiment: Positive")
            elif sentiment == "Neutral":
                st.info("ℹ️ Sentiment: Neutral")
            elif sentiment == "Negative":
                st.error("❌ Sentiment: Negative")
            else:
                st.warning("Could not determine sentiment.")

# Call run() only if this file is run directly
if __name__ == "__main__":
    run()
