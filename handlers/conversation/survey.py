from supabase import Client, create_client
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler

import os
from constants import (
    GET_COUNT,
    GET_NAME,
    GET_QUESTION,
    GET_TYPE,
    GET_OPTIONS,

    SB_KEY,
    SB_URL,
)
import json

# Initialize Supabase client
supabase: Client = create_client(SB_URL, SB_KEY)

async def get_count(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    try:
        count = int(text)
        if count < 1:
            await update.message.reply_text("Please provide a number greater than 0")
            return GET_COUNT
        context.user_data["count"] = count
        context.user_data["questions"] = []
        await update.message.reply_text("Please send the first question")
        return GET_QUESTION
    except ValueError:
        await update.message.reply_text("Please provide a valid number")
        return GET_COUNT


async def get_un_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    names  = (supabase.storage.from_("surveys").list())
    name = update.message.text
    name = name.strip()
    name = name.replace(" ", "_")
    if name in names:
        await update.message.reply_text("This name already exists. Please choose another name.")
        return GET_NAME
    context.user_data["name"] = name
    await update.message.reply_text("Please provide the number of questions in the survey")
    return GET_COUNT


async def get_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    keyboard = [
        [ KeyboardButton("Yes or No") ],
        [ KeyboardButton("Options") ],
        [ KeyboardButton("Text") ],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

    context.user_data["questions"].append({'question': msg})
    await update.message.reply_text(
        "Please choose the type of question",
        reply_markup=reply_markup
    )
    return GET_TYPE

async def get_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.text.lower()
    data = data.lower()

    data = "yes_no" if data == "yes or no" else data

    context.user_data["questions"][-1]['type'] = data
    if data == "options":
        await update.message.reply_text(
            "Please provide the options for the question, separated by hashes (#)\n"
            "Example: option1 # option2 # option3",
            reply_markup=ReplyKeyboardRemove()
        )
        return GET_OPTIONS
    context.user_data["questions"][-1]["options"] = None
    if len(context.user_data["questions"]) == context.user_data["count"]:
        uploadSurveyData(context.user_data)
        await update.message.reply_text("Survey created successfully!", reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    await update.message.reply_text(
        "Please send the next question"
        f"\nQuestion {len(context.user_data['questions']) + 1} of {context.user_data['count']}",
        reply_markup=ReplyKeyboardRemove()
    )
    return GET_QUESTION

async def get_options(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    options = msg.split("#")
    options = [option.strip() for option in options]
    context.user_data["questions"][-1]["options"] = options
    if len(context.user_data["questions"]) == context.user_data["count"]:
        uploadSurveyData(context.user_data)
        await update.message.reply_text("All questions have been added. Creating the survey...")
        return ConversationHandler.END
    await update.message.reply_text("Please send the next question")
    return GET_QUESTION

def uploadSurveyData(data):
    name = data["name"]+"_q.json"
    with open(name, "w") as file:
        json.dump(data, file, indent=4)
    with open(name, 'rb') as file:
        supabase.storage.from_("surveys").upload(name, file)
    os.remove(name)
