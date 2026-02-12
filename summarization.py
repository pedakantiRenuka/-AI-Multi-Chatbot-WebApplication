# import streamlit as st
# import google.generativeai as gen_ai
# from dotenv import load_dotenv
# import os

# # Load environment variables
# load_dotenv()
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# # Configure Gemini AI
# gen_ai.configure(api_key=GOOGLE_API_KEY)
# model = gen_ai.GenerativeModel("gemini-pro")

# # Function to generate a summary using Gemini AI
# def generate_summary(text_input):
#     summary_prompt = f"""
#     Summarize the following text into **clear and concise key points**, ensuring the essence of the content is retained.  
    
#     **Text to Summarize:**
#     {text_input}

#     **Expected Summary Format:**
#     - **Main Idea:** [One sentence summarizing the core message]  
#     - **Key Points:**  
#       - **Highlight 1**  
#       - **Highlight 2**  
#       - **Highlight 3**  
#     - **Conclusion:** [Final takeaway message]  

#     **Summary:**  
#     """
    
#     try:
#         response = model.generate_content(summary_prompt)
#         return response.text.strip() if response else "Error: No summary generated."
#     except Exception as e:
#         return f"Error generating summary: {e}"

# # Function to run the summarization app
# def run():
#     """Runs the Streamlit summarization app."""
#     st.title("📄 Text Summarization")
#     st.write("Enter a paragraph and get a **concise summary with key highlights**.")

#     # Medium-sized text area
#     text_input = st.text_area("Enter the text to summarize:", "", height=200)

#     if st.button("Summarize"):
#         if text_input.strip() == "":
#             st.warning("Please enter some text.")
#         else:
#             summary_text = generate_summary(text_input)
#             st.subheader("📌 Summary:")
#             st.write(summary_text)

# # Run the app when executed directly
# if __name__ == "__main__":
#     run()
import streamlit as st
import google.generativeai as gen_ai
from dotenv import load_dotenv
import os

# Load your Google API Key
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini AI
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel("models/gemini-2.5-flash")

# Function to generate a summary
def generate_summary(text_input):
    prompt = f"""
You are a smart AI summarizer. Convert the following paragraph into a clear and concise summary using Markdown format.

Text to Summarize:
{text_input}

Format your response like this:

### 📌 Summary

**🔹 Main Idea:** (One-line summary)

**🔹 Key Points:**
- 🔸 Point 1  
- 🔸 Point 2  
- 🔸 Point 3  

**🔹 Conclusion:** (Final thought)
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error: {e}"

# Function to run the Streamlit summarizer app
def run():
    st.title("📄 Text Summarization")
    st.write("Paste a paragraph and get a smart summary with a download option.")

    # User input area
    user_input = st.text_area("Enter the text to summarize:", height=200)

    if st.button("Summarize"):
        if user_input.strip() == "":
            st.warning("Please enter some text.")
        else:
            # Generate the summary
            result = generate_summary(user_input)

            # Display summary in styled HTML box
            st.markdown("### 📌 Summary:")
            st.markdown(f"""
<div style="background-color:#f4f4f4; padding: 20px; border-left: 5px solid #C71585; border-radius: 10px;">
{result}
</div>
""", unsafe_allow_html=True)

            # Download button
            st.download_button(
                label="📥 Download Summary",
                data=result,
                file_name="summary.txt",
                mime="text/plain"
            )
if __name__ == "__main__":
    run()
