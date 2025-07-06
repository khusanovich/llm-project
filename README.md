# 🧠 LLM Local Chat with Mistral + Ollama

This project is a minimal example of using a **local Large Language Model (LLM)** with Python and [Ollama](https://ollama.com/). It uses the open-source **Mistral** model to generate text completely offline — no API keys, no cloud, just local power 💪

---

## 🚀 Features

- 🔒 100% offline LLM inference with [Ollama](https://ollama.com/)
- 🧪 Python script to send prompts to the local model
- ✅ Virtual environment with clean setup
- 📁 Git-tracked project structure

---

## 🛠️ Requirements

- Python 3.11+
- [Ollama](https://ollama.com/) installed and running
- Mistral model pulled locally:
  
  ```bash
  ollama pull mistral



✅ What I’ve Done So Far (Recap)
🔧 1. Set Up 
 Local Project Environment
Created a folder: llm-project/

Created a virtual environment (venv) and activated it

Installed required packages like openai and ollama

Created your first Python script (test_openai.py, mistral_chat.py) to use OpenAI and/or Ollama

⚙️ 2. Tested OpenAI and Ollama APIs
Got an error from OpenAI due to API quota limits

Switched to using Ollama locally with models like llama2 (offline, free)

Successfully interacted with the model (mistral_chat.py)

🧠 3. Used Git and GitHub for Version Control
Initialized Git repo

Created and edited .gitignore to exclude venv/ and .env (important)

Pushed the project to GitHub using SSH ✅

📄 4. Created requirements.txt
Added dependencies so others can install them easily using pip install -r requirements.txt
