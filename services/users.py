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
    data, count = (supabase.table("users").select("id").execute())
    data = data[1]
    count = count[1]
    ids = []
    for ur in data:
        ids.append(ur['id'])
    if user.id not in ids:
        supabase.table("users").insert({
            "id": user.id,
            "name": user.full_name,
            "username": user.username,
            "subscribed": True,
        }).execute()
    else:
        print("User already exists in supabase")
    data = {}
    with open('users.json', 'r') as file:
        data = list(json.load(file))
    new_data = {
        "id": user.id,
        "name": user.full_name,
        "username": user.username,
        "subscribed": True,
    }
    data.append(new_data)
    with open('users.json', 'w') as file:
        json.dump(data, file, indent=4)

