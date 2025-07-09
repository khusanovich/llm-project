import gradio as gr
import openai

# Point to your local OpenLLM server
openai.api_base = "http://localhost:3000/v1"
openai.api_key = "sk-fake-key"  # Needed, even if not checked

def chat(message, history):
    if history is None:
        history = []

    print("User:", message)

    messages = history + [{"role": "user", "content": message}]

    response = openai.ChatCompletion.create(
        model="llama2",  # Match the model you started with `openllm start llama2`
        messages=messages
    )
    assistant_reply = response["choices"][0]["message"]["content"]
    print("Bot:", assistant_reply)

    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": assistant_reply})

    return "", history

if __name__ == "__main__":
    gr.ChatInterface(
        fn=chat,
        chatbot=gr.Chatbot(type="messages"),
        textbox=gr.Textbox(placeholder="Ask anything...", container=True, scale=7),
        title="🦙 Local LLM Chat",
        description="Chat with your local LLM using OpenLLM",
        theme="soft",
        examples=["What is the capital of Uzbekistan?", "Explain quantum computing in simple terms"],
        cache_examples=False,
        # Buttons removed since gradio 5.35.0 doesn't support retry/undo args
        # retry_btn="🔁 Retry",
        # undo_btn="↩️ Undo",
        # clear_btn="🧹 Clear",
    ).launch()

