# Imports
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ExtBot, ConversationHandler
from handlers.branch.start import start_init
from services.users import registerUser
from services.telegram import checkCommandProceed, reportError
from constants import (
    ADMINS, 
    OWNER,

    GET_NAME,
    GET_OPTIONS,
    GET_QUESTION,
    GET_TYPE,
)

# Main start command handler function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        canProceed = await checkCommandProceed(update, context)
        if not canProceed:
            return
        mode = context.args[0] if context.args else ''
        if mode == '':
            await update.message.reply_text("May Allah bless you")
            await registerUser(update.effective_user, context.bot)
        elif mode == 'INIT':
            await start_init(update, context.bot)
    except Exception as e:
        await reportError(context.bot, e, update.effective_user)
        
# Command to delete messages
async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # try and if exception occurs, report it to owner
    try:
        # user's id
        user_id = update.effective_user.id
        if str(user_id) not in ADMINS:
            # delete the message if user is not an admin
            await update.message.delete()
            return
        length = len(context.args)
        if length == 0:
            # delete the message if no arguments are provided
            await update.message.delete()
            return
        if length > 2:
            # delete the message if more than 2 arguments are provided
            await update.message.delete()
            return
        intArgs = []
        for arg in context.args:
            try:
                intArgs.append(int(arg))
            except ValueError:
                # delete the message if argument is not an integer
                await update.message.delete()
                return
        startid = update.message.id  if len(intArgs) == 1 else update.message.id - intArgs[1]
        await update.message.delete()
        ids = range(startid - intArgs[0], startid)
        await context.bot.delete_messages(
            update.effective_chat.id,
            ids,
        )
    except Exception as e:
        await reportError(context.bot, e, update.effective_user)

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

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Cancelled")
    return ConversationHandler.END

async def newsurvey(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if the command can proceed - type of chat
    canProceed = await checkCommandProceed(update, context)
    if not canProceed:
        return ConversationHandler.END
    
    # Check if the user is an admin
    user = str(update.effective_user.id)
    if user not in ADMINS:
        await update.message.reply_text("You are not authorized to use this command")
        return ConversationHandler.END
    
    await update.message.reply_text("Please provide a name for the survey (should be unique)")
    return GET_NAME
