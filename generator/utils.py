# generator/utils.py

import requests
import base64

# Updated API URL for Stable Diffusion 3.5 Large model
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
HUGGINGFACE_API_TOKEN = "add your huggiface api key"  # Use your API token

headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}",
    "Content-Type": "application/json"
}

def generate_anime_image(prompt):
    payload = {
        "inputs": prompt,
        "options": {"use_gpu": True},  # Optional: Use GPU if supported
    }

    response = requests.post(HUGGINGFACE_API_URL, headers=headers, json=payload, timeout=60)

    # Handle the response
    if response.status_code != 200:
        raise Exception(f"Failed to generate image: {response.text}")

    image_bytes = response.content
    img_base64 = base64.b64encode(image_bytes).decode()

    return img_base64  # Return the base64 encoded image
