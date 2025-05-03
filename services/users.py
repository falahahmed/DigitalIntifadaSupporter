# imports
from telegram import User
import json
from supabase import Client, create_client
from constants import SB_KEY, SB_URL

# Initialize Supabase client
supabase: Client = create_client(SB_URL, SB_KEY)


# Function to register a new user
def registerUser(user: User) -> None:
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
    else:
        # user already exists in supabase
        print("User already exists in supabase")
