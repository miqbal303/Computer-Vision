import streamlit as st
import requests
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
GOOGLE_API_KEY = os.getenv('KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Function to query the Blip Image Captioning model
def query_blip_image_captioning(filename):
    try:
        API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
        headers = headers = {"Authorization": "Bearer {Auth_Token}"}  # Authorization Token
        response = requests.post(API_URL, headers=headers, data=filename)
        return response.json()
    except Exception as e:
        st.error(f"An error occurred while querying the Blip Image Semantic model: {e}")

# Function to query the Mixtral model
def query_mixtral(payload):
    try:
        API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
        headers = {"Authorization": "Bearer {Auth_Token}"}  # Authorization Token
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    except Exception as e:
        st.error(f"An error occurred while querying the Mixtral Captioning model: {e}")

# Function to generate caption using Gemini model
def generate_caption(input_text):
    try:
        response = model.generate_content(input_text)
        caption = response.text
        return caption
    except Exception as e:
        st.error(f"An error occurred while generating caption: {e}")
        return None

# Streamlit app
def main():
    st.title("📷 Image Semantic and Caption Generator 📝")

    # Upload image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read file data
        image_data = uploaded_file.read()

        # Query the Blip Image Captioning model
        blip_output = query_blip_image_captioning(image_data)
        blip_text = blip_output[0]["generated_text"] if blip_output is not None else ""

        # Query the Mixtral model for Captioning
        mixtral_payload = {
            "inputs": f"{blip_text} to an instagram captioning for my post make sure add hashtag and emojis Answer:"
        }
        mixtral_output = query_mixtral(mixtral_payload)
        mixtral_caption = mixtral_output[0]["generated_text"] if mixtral_output is not None else ""

        # Generate caption using Gemini model
        input_text = f"{blip_text} to create an Instagram post with hashtags and emojis."
        caption_gemini = generate_caption(input_text)

        # Display the image and generated captions in horizontal layout
        
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("Semantic:")
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        with col1:
            if blip_text:
                st.markdown(
                    f'<div style="border: 2px solid black; border-radius: 10px; padding: 10px; font-family: Arial, sans-serif;">{blip_text}</div>',
                    unsafe_allow_html=True)

        with col2:
            if mixtral_caption:
                st.subheader("Mixtral Caption")
                st.markdown(
                    f'<div style="border: 2px solid black; border-radius: 10px; padding: 10px; font-family: Arial, sans-serif;">{mixtral_caption}</div>',
                    unsafe_allow_html=True)

        with col3:
            if caption_gemini:
                st.subheader("Gemini Caption")
                st.markdown(
                    f'<div style="border: 2px solid black; border-radius: 10px; padding: 10px; font-family: Arial, sans-serif;">{caption_gemini}</div>',
                    unsafe_allow_html=True)


if __name__ == "__main__":
    main()
