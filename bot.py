# Module imports
from constants import API_KEY
from handlers.command import start

# Standard library imports
import logging

# ptb imports
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)



# Main function to handle application startup
def main():
    # Creating a bot instance
    bot = ApplicationBuilder().token(API_KEY).build()

    # Command Handlers
    bot.add_handler(CommandHandler("start", start))

    # Starting the bot
    bot.run_polling()


# Initial function call
if __name__ == "__main__":
    main()