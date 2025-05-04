# imports
from telegram import User
from telegram.constants import ParseMode
from telegram.ext import ExtBot
from supabase import Client, create_client
from constants import SB_KEY, SB_URL, LOGS

# Initialize Supabase client
supabase: Client = create_client(SB_URL, SB_KEY)


# Function to register a new user
async def registerUser(user: User, bot:ExtBot) -> None:
    # get data from supabase
    response = supabase.table("users").select("id").execute()
    data = response.data
    count = response.count

    # ids in the supabase
    ids = []
    for ur in data:
        ids.append(ur['id'])

    #  add user to supabase if not already present
    if user.id not in ids:
        supabase.table("users").insert({
            "id": user.id,
            "name": user.full_name,
            "username": user.username,
            "subscribed": True,
        }).execute()
        if LOGS != None:
            message = f"User <a href='t.me/{user.username}'>{user.full_name}</a> has subscribed to the bot"
            if user.username!= None:
                f"User {user.full_name} has subscribed to the bot (id: {user.id})",
                    
            await bot.send_message(
                LOGS, 
                message,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )
    else:
        # user already exists in supabase
        print("User already exists in supabase")
