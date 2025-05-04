import dotenv
import os

path = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_path=path)

API_KEY = os.environ.get("API_KEY")

CHAT_ID = os.environ.get("CHAT_ID")

ADMINS:list = os.environ.get("ADMINS")

BOT = os.environ.get("BOT")

SB_URL = os.environ.get("SB_URL")

SB_KEY = os.environ.get("SB_KEY")

LOGS = os.environ.get("LOGS")