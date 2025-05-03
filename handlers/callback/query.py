# imports
from telegram import Update
from telegram.ext import ContextTypes
from services.users import cleanUserData

async def callbackQueries(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    data = query.data
    if data == "users":
        cleanUserData()
        await query.edit_message_text("Duplicates in users data cleaned")