import dotenv
import os

path = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_path=path)

API_KEY = os.getenv("API_KEY").replace("\\x3a", ":").replace("\\x2f", "/")

CHAT_ID = os.getenv("CHAT_ID").replace("\\x3a", ":").replace("\\x2f", "/")

ADMINS:list = os.getenv("ADMINS").replace("\\x3a", ":").replace("\\x2f", "/")

BOT = os.getenv("BOT").replace("\\x3a", ":").replace("\\x2f", "/")

SB_URL = os.getenv("SB_URL").replace("\\x3a", ":").replace("\\x2f", "/")

SB_KEY = os.getenv("SB_KEY").replace("\\x3a", ":").replace("\\x2f", "/")

LOGS = os.getenv("LOGS").replace("\\x3a", ":").replace("\\x2f", "/")

OWNER = os.getenv("OWNER").replace("\\x3a", ":").replace("\\x2f", "/")