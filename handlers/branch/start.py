# imports
from telegram import Update
from telegram.ext import ContextTypes, ExtBot
from services.users import registerUser

# Initial start handler
async def start_init(update: Update, bot: ExtBot) -> None:
    link = "https://docs.google.com/forms/d/e/1FAIpQLSeVlZGc_VFMh9Urau1_BtG58FIpXYl0a2ab2NrgkB66jeMdSw/viewform?usp=sharing"
    await update.message.reply_text(link)
    await registerUser(update.effective_user, bot)