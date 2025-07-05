from ollama import Client

client = Client()

response = client.chat(
    model='mistral',
    messages=[
        {"role": "user", "content": "How does photosynthesis work?"}
    ]
)

print(response['message']['content'])


