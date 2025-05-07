# imports
from telegram import Update, User
from telegram.ext import ContextTypes, ExtBot
from constants import BOT, OWNER

# Function to check if the command can proceed
async def checkCommandProceed(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    # Command can proceed if the chat is private
    if update.effective_chat.type == "private":
        return True
    else:
        # Send the user a personal message and remove the command from the group

        # id of user
        user_id = update.effective_user.id
        # command from user
        commands = update.message.text.strip().split(" ")
        command = commands[0]
        # Sending the user a personal message
        try:
            await context.bot.send_message(
                chat_id=user_id, 
                text=f"Assalamu Alaikkum, I am not supposed to chat in groups. We can continue here.\n Your command: {command}",
            )
        except:
            pass
        # Deleting the command from user in the group
        await update.message.delete()
        # returning false - don't interact with it
        return False
    

async def reportError(bot: ExtBot, error: Exception, user: User) -> None:
    await bot.send_message(
        OWNER,
        f"Error occured:{error}\nUser: {user.id}\nName: {user.first_name}\nUsername: {user.username}",
    )