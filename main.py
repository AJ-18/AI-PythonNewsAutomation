# Short Email News App by AJ:
import os
import requests
import time
from dotenv import load_dotenv
from send_email import send_email
from langchain.chat_models import init_chat_model

# Load the env file for the API key
load_dotenv()

# Wait before sending another request
time.sleep(1)
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

url = (f"https://newsapi.org/v2/top-headlines?"
       f"category=business&"
       f"country=us&"
       f"pageSize=8&"
       f"sortBy=publishedAt&apiKey={NEWS_API_KEY}")

# Header to get the request, act like a user
headers = {"User-Agent": "Mozilla/5.0"}

# Make the request
request = requests.get(url, headers=headers)

# Store the response as json
content = request.json()
articles = content["articles"]
print(articles)


# AI summarizing the news
model = init_chat_model(
    model="gemini-3-flash-preview",
    model_provider="google-genai",
    api_key=GEMINI_API_KEY
)
prompt = f"""
You are a news summarizer. 
Write a short paragraph analyzing those news articles
and add another paragraph to tell me how they affect the stock market.
Here are the news articles:
{articles}

"""

response = model.invoke(prompt)
response_str = response.content[0]['text']
print(response_str)

body = "Subject: New Summary\n\n" + response_str + "\n\n"
print(body)

body = body.encode("utf-8")
send_email(body)