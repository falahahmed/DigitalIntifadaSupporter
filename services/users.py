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
        "isSub": True
    }
    data.append(new_data)
    with open('users.json', 'w') as file:
        json.dump(data, file, indent=4)