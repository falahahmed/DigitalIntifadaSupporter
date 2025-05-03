# imports
from telegram import User
import json

# Function to register a new user
def registerUser(user: User) -> None:
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

# Function to clean the user data file - Removing duplicates
def cleanUserData() -> None:
    data = {}
    with open('users.json', 'r') as file:
        data = list(json.load(file))
    unique_data = []
    seen_ids = set()
    for user in data:
        if user['id'] not in seen_ids:
            unique_data.append(user)
            seen_ids.add(user['id'])
    with open('users.json', 'w') as file:
        json.dump(unique_data, file, indent=4)