# Module imports
from constants import API_KEY
from handlers.command import start, clean
from handlers.joinRequest import join_request
from handlers.callback.query import callbackQueries

# Standard library imports
import logging

# ptb imports
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, 
    CommandHandler,
    ChatJoinRequestHandler,
    CallbackQueryHandler,
    filters,
)


# Setting the default filter for commands - personal chat
privateChat = filters.ChatType.PRIVATE

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
    bot.add_handler(CommandHandler("clean", clean))

    # Callback Query Handlers
    bot.add_handler(CallbackQueryHandler(callbackQueries))

    # Join request handler
    bot.add_handler(ChatJoinRequestHandler(join_request))

    # Starting the bot
    bot.run_polling()


# Initial function call
if __name__ == "__main__":
    main()