# imports
from telegram import Update
from telegram.ext import ContextTypes

async def callbackQueries(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    data = query.data
    pass