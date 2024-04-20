from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

try:
    print("Testing ChatGroq initialization...")
    groq_test = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768",groq_api_key=os.getenv("GROQ_API_KEY"))
    print("ChatGroq initialized successfully.")
except Exception as e:
    print("Failed to initialize ChatGroq:", e)