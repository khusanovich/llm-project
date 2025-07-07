import gradio as gr
from ollama import Client

client = Client()

def chat_fn(messages):
    # messages = list of dicts like: {"role": "user", "content": "..."}
    response = client.chat(model="llama2", messages=messages)
    return response['message']['content']

gr.ChatInterface(
    fn=chat_fn,
    chatbot=gr.Chatbot(),
    textbox=gr.Textbox(placeholder="Ask me anything..."),
    title="Llama2 Chat",
    theme="soft",
    examples=["What is photosynthesis?", "Tell me a joke"],
    retry_btn="🔁 Retry",
    clear_btn="🗑️ Clear",
).launch()

