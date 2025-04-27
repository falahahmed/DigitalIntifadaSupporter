# Imports
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ExtBot
from handlers.branch.start import start_init
from services.users import registerUser
from constants import ADMINS

# Main start command handler function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mode = update.message.text[7:]
    if mode == '':
        await update.message.reply_text("May Allah bless you")
        registerUser(update.effective_user)
    elif mode == 'INIT':
        await start_init(update, context.bot)
        

async def clean(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = str(update.effective_user.id)
    if user not in ADMINS:
        await update.message.reply_text("You are not authorized to use this command")
        return
    keyboard = [
        [InlineKeyboardButton("Duplicates in users data", callback_data="users")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("What should I clean?", reply_markup=reply_markup)
