import gradio as gr
from datetime import datetime
from ollama import Client

client = Client()

def chat_with_model(message, history):
    full_history = "\n".join([f"User: {user}\nAI: {bot}" for user, bot in history])
    prompt = f"{full_history}\nUser: {message}\nAI:"
    response = client.chat(model="llama2", messages=[{"role": "user", "content": prompt}])
    reply = response['message']['content']

    # Optional: log to file with timestamp
    with open("chat_log.txt", "a") as f:
        f.write(f"{datetime.now()} - USER: {message}\n")
        f.write(f"{datetime.now()} - BOT: {reply}\n\n")

    return reply

gr.ChatInterface(fn=chat_with_model, title="Llama2 Chat with Ollama").launch()

