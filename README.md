# Gemini API Chat Project

This project provides a simple Python interface to interact with Google's *Gemini* API using the ⁠ google-generativeai ⁠ SDK. It includes:

•⁠  ⁠A basic prompt-response example (⁠ gemini_api.py ⁠)

•⁠  ⁠An interactive terminal-based chat session with memory (⁠ terminal_memory_chat.py ⁠)

•⁠  ⁠A utility to manage environment variables (⁠ utils.py ⁠)

---

## 📦 Installation

1.⁠ ⁠*Clone the repository*

    ⁠ bash
    git clone https://github.com/avivlaufman/GeminiAPI
    cd GeminiAPI
     ⁠

2.⁠ ⁠*Create a virtual environment (recommended)*

    ⁠ bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
     ⁠

3.⁠ ⁠*Install the dependencies*

    ⁠ bash
    pip install -r requirements.txt
     ⁠

---

## 🔑 Setup: API Key

1.⁠ ⁠Create a ⁠ .env ⁠ file in the root directory of the project.

2.⁠ ⁠Add your [Google Gemini API key](https://makersuite.google.com/app/apikey) to the ⁠ .env ⁠ file like this:

    ⁠ dotenv
    API_KEY=your_actual_api_key_here
     ⁠

---

## 🚀 Running the Scripts

### 1. Simple Prompt Example

Run the ⁠ gemini_api.py ⁠ script to send a single prompt to Gemini and print the response:

```bash
python gemini_api.py
```
Example:     

prompt = "Explain how AI works in a few words"

### 2. Multi-turn Gemini API chat

Run the ⁠ terminal_memory_chat.py ⁠ script to start a conversation through the terminal:

```bash
python terminal_memory_chat.py
```
Example:     

First Turn: How much is 2X3?

Second Turn: Multiply it by 4

Final turn: exit

