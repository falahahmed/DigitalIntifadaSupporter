#  Imports
from telegram import Update, User
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

from constants import CHAT_ID, BOT

# Join request handler function
async def join_request(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    # Check if the Chat is the correct one
    chat_id = str(update.effective_chat.id)
    if chat_id != CHAT_ID:
        return

    # Send message to user before approving the join request
    # Get the text to send to user
    message = formatMessage(update.effective_user.first_name)
    await context.bot.send_message(
        chat_id=update.effective_user.id, 
        text=message,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )
    await update.chat_join_request.approve()


# Function to format the message
def formatMessage(name: str) -> str:
    msg = ""
    msg += f"Assalamu Alaikkum {name},\n"
    msg += "Welcome to the Digital Intifada!\n"
    msg += "We have slowly but firmly started our project. We would like to know more about you and the "
    msg += "fields you can contribute in. "
    msg += f"Please click <a href='https://t.me/{BOT}?start=INIT'>here</a> to get the form.\n"
    msg += "<b>Thank  you and May Allah bless you.</b>\n"

    return msg