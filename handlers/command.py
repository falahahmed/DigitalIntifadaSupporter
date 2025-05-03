# Imports
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ExtBot
from handlers.branch.start import start_init
from services.users import registerUser
from services.telegram import checkCommandProceed
from constants import ADMINS

# Main start command handler function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    canProceed = await checkCommandProceed(update, context)
    if not canProceed:
        return
    mode = update.message.text[7:]
    if mode == '':
        await update.message.reply_text("May Allah bless you")
        registerUser(update.effective_user)
    elif mode == 'INIT':
        await start_init(update, context.bot)
        

# Function to clean the data related to users, etc.
async def clean(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if the command can proceed - type of chat
    canProceed = await checkCommandProceed(update, context)
    if not canProceed:
        return
    
    # Check if the user is an admin
    user = str(update.effective_user.id)
    if user not in ADMINS:
        await update.message.reply_text("You are not authorized to use this command")
        return
    
    # Options to clean
    keyboard = [
        [InlineKeyboardButton("Duplicates in users data", callback_data="users")],
    ]
    # Markup and reply
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("We are working on it")
