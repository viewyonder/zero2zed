import anthropic
import os
from dotenv import load_dotenv

# Set your Anthropic API key. In practice, use environment variables for security.
# Here, I'm using a placeholder. You should replace this with your actual key or load from an environment variable.
# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
API_KEY = os.getenv('ANTHROPIC_API_KEY')

if not API_KEY:
    raise ValueError("No API key found. Please set the ANTHROPIC_API_KEY environment variable.")

# Initialize the client with your API key
client = anthropic.Anthropic(api_key=API_KEY)

# Define the question you want to ask
question = "What is the capital of England?"

# Use the Claude-3 model to ask your question
try:
    response = client.messages.create(
        model="claude-3-5-haiku-latest",  # or use another model like "claude-3-sonnet"
        max_tokens=300,
        messages=[
                    {
                        "role": "user",
                        "content": question
                    }
                ]
    )

    # Print the answer from the AI
    print(response.content[0].text)

except anthropic.APIError as e:
    print(f"An API error occurred: {e}")
except anthropic.AuthenticationError:
    print("Authentication failed. Please check your API key.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
