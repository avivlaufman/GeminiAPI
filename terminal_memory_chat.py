import google.generativeai as genai
from google.generativeai import GenerativeModel

from utils import load_api_key


def generate_response(model: GenerativeModel, chat_history: list) -> str:
    """
    Send the chat history to the Gemini API and get a response.

    Args:
        client (genai.Client): The Gemini API client.
        chat_history (list): List of messages exchanged in the chat.

    Returns:
        str: The model's response text.
    """
    response = model.generate_content(chat_history)
    return response.text


def start_terminal_chat():
    """
    Start a terminal-based chat with the Gemini model.
    """
    api_key = load_api_key()
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")
    chat_history = []

    print("=== Welcome to the Gemini Terminal Chat ===")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Add user input to chat history
        chat_history.append({"role": "user", "parts": user_input})

        # Generate response and add it to chat history
        model_response = generate_response(model, chat_history)
        print("Gemini:", model_response)
        chat_history.append({"role": "model", "parts": model_response})


if __name__ == "__main__":
    start_terminal_chat()
