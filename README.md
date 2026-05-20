Ollama Streamlit Chatbot

A simple AI chatbot built using Streamlit and Ollama.

This project allows you to run local Large Language Models (LLMs) like gemma:2b, llama3, mistral, and more directly from your computer.

 Features
Simple Streamlit UI
Local AI model execution using Ollama
Fast response generation
Lightweight and beginner-friendly
Supports multiple Ollama models
 Project Structure
project-folder/
│
├── app.py
├── README.md
└── requirements.txt
 Technologies Used
Python
Streamlit
Ollama
 Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/ollama-streamlit-chatbot.git

cd ollama-streamlit-chatbot
2️⃣ Create Virtual Environment (Optional)
Windows
python -m venv venv

venv\Scripts\activate
Linux / Mac
python3 -m venv venv

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
 Install Ollama

Download and install Ollama:

https://ollama.com/download

 Pull a Model

Example:

ollama pull gemma:2b

You can also use:

ollama pull llama3
ollama pull mistral
▶️ Run Ollama

Start the model:

ollama run gemma:2b
▶️ Run Streamlit App
streamlit run app.py
💻 Example Code
from ollama import Client

client = Client(host="http://localhost:11434")

response = client.chat(
    model="gemma:2b",
    messages=[
        {"role": "user", "content": "Hello"}
    ]
)

print(response["message"]["content"])
