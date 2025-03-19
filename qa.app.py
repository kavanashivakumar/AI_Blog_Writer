from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

# Configure the generative AI client
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the generative model
model = genai.GenerativeModel("gemini-1.5-flash") 

# Function to get a response from Gemini
def get_gemini_response(topic, no_words, audience):
    question = f"Write a blog for {audience} on the topic '{topic}' within {no_words} words."
    response = model.generate_content(question)
    parts = response.candidates[0].content.parts
    text = ' '.join(part.text for part in parts)
    return text 

# Streamlit application setup
st.set_page_config(page_title="Generate Blogs", page_icon='🤖', layout='centered', initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

# Creating two more columns for additional fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('Number of Words')

with col2:
    blog_audience = st.text_input(
        'Writing the blog for (e.g., Common People, Researchers, Teachers)',
        key="blog_audience"
    )

submit = st.button("Generate")

# Final response
if submit:
    if input_text and no_words and blog_audience:
        response = get_gemini_response(input_text, no_words, blog_audience)
        st.subheader("Generated Blog")
        st.write(response)
    else:
        st.error("Please fill in all the fields.")
