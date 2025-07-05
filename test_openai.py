import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load .env file
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say hello from the LLM project!"}
    ]
)

print(response.choices[0].message.content)


