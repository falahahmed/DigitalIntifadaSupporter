import dotenv
import os

path = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_path=path)

API_KEY = os.environ.get("API_KEY")

CHAT_ID = os.environ.get("CHAT_ID")