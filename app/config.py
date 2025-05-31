# from dotenv import load_dotenv
# import os
# from pathlib import Path

# # Get the root directory of the project
# ROOT_DIR = Path(__file__).resolve().parent.parent.parent

# # Construct the path to the .env file
# env_file = ROOT_DIR / ".env"

# # Ensure .env file exists before loading it
# if not env_file.exists():
#     raise FileNotFoundError(f".env file not found at {env_file}")

# # Load environment variables from .env file
# load_dotenv(env_file)

# # Get Groq API key with error handling
# def get_groq_api_key():
#     api_key = os.getenv("GROQ_API_KEY")
#     if not api_key:
#         raise ValueError("GROQ_API_KEY not found in environment variables")
#     return api_key


from dotenv import load_dotenv
import os
from pathlib import Path

# Get the root directory of the project
ROOT_DIR = Path(__file__).resolve().parent.parent

# Construct the path to the .env file
env_file = ROOT_DIR / ".env"

# Load environment variables from .env file if it exists (for local dev)
load_dotenv(env_file)

# Get Groq API key with error handling
def get_groq_api_key():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")
    return api_key
