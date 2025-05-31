from google import genai
from utils import load_api_key


def main():
    """
    Generate a response from Gemini based on a simple prompt.
    """
    # Load API key
    api_key = load_api_key()

    # Initialize the Gemini client
    client = genai.Client(api_key=api_key)

    # Prompt to be sent to Gemini
    prompt = "Explain how AI works in a few words"

    # Generate the response
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    # Print the response
    print("Gemini Response:")
    print(response.text)


if __name__ == "__main__":
    main()
