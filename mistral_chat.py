from ollama import Client
from datetime import datetime

client = Client()

# Open a log file in append mode
log_file_path = "chat_log.txt"

def log_message(role, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file_path, "a") as log_file:
        log_file.write(f"[{timestamp}] {role}: {message}\n")

# Logging conversation
log_message("User: What is photosynthesis?")
log_message("AI: Photosynthesis is a process...")

while True:
    user_input = input("You: ")
    if user_input.lower() in {"exit", "quit"}:
        print("Chat ended.")
        break

    log_message("You", user_input)

    response = client.chat(model="llama2", messages=[
        {"role": "user", "content": user_input}
    ])

    bot_reply = response['message']['content']
    print("Bot:", bot_reply)

    log_message("Bot", bot_reply)

