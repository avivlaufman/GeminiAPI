import os

from dotenv import load_dotenv


def load_api_key() -> str:
    """
    Load the API key from the .env file.

    Returns:
        str: The API key.
    """
    load_dotenv()
    api_key = os.getenv('API_KEY')
    if not api_key:
        raise ValueError("API_KEY not found in environment variables.")
    return api_key
