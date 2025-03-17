import os
import requests
from fastapi import APIRouter
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/v1/chat/completions"  

@router.get("/generate-text")
def generate_text(prompt: str, max_length: int = 800):
    """
    Calls the Groq API to generate text based on the provided prompt using Mistral.
    """
    payload = {
        "model": "mistral-7b",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_length
    }
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(GROQ_API_URL, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()  
    else:
        return {"error": response.text}
