# Module imports
from constants import (
    API_KEY,

    GET_COUNT,
    GET_OPTIONS,
    GET_NAME,
    GET_QUESTION,
    GET_TYPE,
    SURVEY_ERROR
)
from handlers.command import (
    start, 
    clean, 
    delete, 
    cancel,
    newsurvey,
)
from handlers.conversation.survey import (
    get_count, 
    get_un_name,
    get_question,
)
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
    MessageHandler,
    ConversationHandler,
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
    bot.add_handler(CommandHandler("del", delete))

    # Callback Query Handlers
    bot.add_handler(CallbackQueryHandler(callbackQueries))

    # Conversation Handler
    bot.add_handler(newsurvey_handler)

    # Join request handler
    bot.add_handler(ChatJoinRequestHandler(join_request))

    # Starting the bot
    bot.run_polling()


newsurvey_handler = ConversationHandler(
    entry_points=[CommandHandler("newsurvey", newsurvey)],
    states={
        GET_NAME : [MessageHandler(filters.TEXT & ~filters.COMMAND, get_un_name)],
        GET_COUNT : [MessageHandler(filters.TEXT & ~filters.COMMAND, get_count)],
        GET_QUESTION : [MessageHandler(filters.TEXT & ~filters.COMMAND, get_question)],
    },
    fallbacks=[
        CommandHandler("cancel", cancel),
    ],
)

# Initial function call
if __name__ == "__main__":
    main()