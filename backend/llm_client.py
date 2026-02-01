import requests
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


class LLMClient:
    def __init__(self):
        self.url = "https://api.groq.com/openai/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

    def generate(self, prompt, max_tokens=300):
        payload = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.5,
            "max_tokens": max_tokens
        }

        response = requests.post(self.url, headers=self.headers, json=payload)

        if response.status_code != 200:
            raise Exception(response.text)

        return response.json()["choices"][0]["message"]["content"]


# Test
if __name__ == "__main__":
    client = LLMClient()
    print(client.generate("Explain why good battery life matters in a phone."))
