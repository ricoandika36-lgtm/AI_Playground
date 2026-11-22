from openai import OpenAI
from core.config import API_KEY

def create_client():
    if not API_KEY:
        raise ValueError("API Key belum dikonfigurasi")

    return OpenAI(api_key=API_KEY)
