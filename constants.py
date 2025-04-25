import dotenv
import os

vars = dotenv.load_dotenv(dotenv_path=".env")
API_KEY = os.environ.get("API_KEY")
