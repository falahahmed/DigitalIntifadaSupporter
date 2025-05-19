from supabase import Client, create_client
from telegram import Update
from telegram.ext import ContextTypes

from constants import (
    GET_COUNT,
    GET_NAME,
    GET_QUESTION,

    SB_KEY,
    SB_URL,
)

# Initialize Supabase client
supabase: Client = create_client(SB_URL, SB_KEY)

async def get_count(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    try:
        count = int(text)
        if count < 1:
            await update.message.reply_text("Please provide a number greater than 0")
            return GET_COUNT
        context.user_data["count"] = count
        context.user_data["questions"] = []
        await update.message.reply_text("Please send the first question")
        return GET_QUESTION
    except ValueError:
        await update.message.reply_text("Please provide a valid number")
        return GET_COUNT


async def get_un_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    names  = (supabase.storage.from_("surveys").list())
    name = update.message.text
    name = name.strip()
    name = name.replace(" ", "_")
    if name in names:
        await update.message.reply_text("This name already exists. Please choose another name.")
        return GET_NAME
    context.user_data["name"] = name
    await update.message.reply_text("Please provide the number of questions in the survey")
    return GET_COUNT


async def get_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass