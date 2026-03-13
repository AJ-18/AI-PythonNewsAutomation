import os
import requests
import time
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

model = init_chat_model(
    model="gemini-3-flash-preview",
    model_provider="google-genai",
    api_key=GEMINI_API_KEY
)

response = model.invoke("When should you use a pen versus a pencil?")
response_str = response.content[0]['text']
print(response_str)