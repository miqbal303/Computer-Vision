import streamlit as st
import os
import requests
from dotenv import load_dotenv
from pymongo import MongoClient
import logging
import csv

# Load environment variables from .env file
load_dotenv()

# access the environment variables
GOOGLE_API_KEY = os.getenv('KEY')
mongo_url = os.getenv('mongo_url')

# MongoDB connection
client = MongoClient(mongo_url)  # Update with your MongoDB connection string
db = client["gemini_db"]  # Update with your database name
collection = db["searches"]  # Update with your collection name

# Setup logging
logging.basicConfig(filename='app.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.ERROR)

# Define the function ask_gemini_with_generative_model
def ask_gemini_with_generative_model(question):
    """
    Sends a question to the Gemini API and returns the answer.
    """
    try:
        import google.generativeai as genai
        
        # Configure the GenerativeAI API with your API key
        genai.configure(api_key=GOOGLE_API_KEY)
        
        # Create a GenerativeModel object with the desired model (e.g., 'gemini-pro')
        model = genai.GenerativeModel('gemini-pro')
        
        # Generate content based on the question
        response = model.generate_content(question)
        
        return response.text
    except Exception as e:
        logging.error(f"Error in ask_gemini_with_generative_model: {str(e)}")
        return "Sorry, an error occurred while processing your question."

# Function to save data to CSV
def save_to_csv(question, answer):
    # Remove newline characters from the answer
    answer = answer.replace('\n', ' ')
    with open('searches.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        # Check if the file is empty, if yes, write header
        if file.tell() == 0:
            writer.writerow(['Search Words', 'Gemini Answer'])
        writer.writerow([question, answer])



# Streamlit app
def main():
    st.title("Powered By Gemini")
    question = st.text_input("Enter your question here:")
    
    if st.button("Ask"):
        if len(question.strip()) > 0:
            try:
                answer = ask_gemini_with_generative_model(question)
                st.write("Answer:")
                st.write(answer)
                
                # Store the question and answer in MongoDB
                search_entry = {"question": question, "answer": answer}
                collection.insert_one(search_entry)
                
                # Save to CSV
                save_to_csv(question, answer)
                
                #st.write("Search stored in MongoDB successfully!")
            except Exception as e:
                st.error("An error occurred while processing your request. Please try again later.")
                logging.error(f"Error in main: {str(e)}")

if __name__ == "__main__":
    main()
