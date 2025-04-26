# Imports
from telegram import Update
from telegram.ext import ContextTypes, ExtBot
from services.users import registerUser

# Main start command handler function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mode = update.message.text[7:]
    if mode == 'INIT':
        await start_init(update, context.bot)
        

# Initial start handler
async def start_init(update: Update, bot: ExtBot) -> None:
    link = "https://docs.google.com/forms/d/e/1FAIpQLSeVlZGc_VFMh9Urau1_BtG58FIpXYl0a2ab2NrgkB66jeMdSw/viewform?usp=sharing"
    await update.message.reply_text(link)
    registerUser(update.effective_user)
