import requests
from config.host import OLLAMA_URL

def get_chat_response(prompt: str):
    payload = {"model": "deepseek-r1:latest", "prompt": prompt, "stream": False}

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to connect to chatbot: {str(e)}"}

