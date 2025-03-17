import os
import requests
from fastapi import APIRouter
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

HF_API_KEY = os.getenv("HF_ACCESS_TOKEN")
HF_IMAGE_MODEL_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"

@router.get("/generate-image")
def generate_image(prompt: str, num_inference_steps: int = 25):
    """
    Calls the Hugging Face Inference API to generate an image based on the prompt.
    """
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {
        "inputs": prompt,
        "options": {"wait_for_model": True},
        "parameters": {"num_inference_steps": num_inference_steps}
    }
    response = requests.post(HF_IMAGE_MODEL_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        return {"error": response.text}
