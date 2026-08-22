"""
this bot in telegram with id @Reminder_amir_bot .
This bot is designed to send daily reminders.
"""

# Using the Telegram Bot Library
import os
from datetime import time  # To send an automated reminder at a specific time
from zoneinfo import ZoneInfo  # To determine the location for the clock

from dotenv import load_dotenv  # for hidden token
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from database import Database  #To connect to the database

load_dotenv()
db = Database()

# Obtaining a token from BotFather
TOKEN = os.getenv("TOKEN")

TEXT, TIME = range(2)

# reminder function for auto reminder in bot
async def reminder (context : ContextTypes.DEFAULT_TYPE):
    chat_id = context.job.chat_id
    await context.bot.send_message(
        chat_id = chat_id ,
        text = "وقتش رسید"
    )

# Start function for /start in bot

async def post_init (application):
    users = db.get_users()

    for user in users:
        chat_id = user[0]

        name = f"reminder_{chat_id}"

        application.job_queue.run_daily(
            reminder,
            time=time(
                hour=14,
                minute=10,
                tzinfo=ZoneInfo("Asia/Tehran")
            ),
            chat_id=chat_id,
            name=name
        )
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # async 

    chat_id = update.effective_chat.id
    db.add(chat_id)
    print("job created", chat_id)

    name = f"reminder_{chat_id}"
    old_jobs = context.job_queue.get_jobs_by_name(name)
    for job in old_jobs:
        job.schedule_removal()


    job = context.job_queue.run_daily(
        reminder,
    
    time=time(hour=14, minute=10 , tzinfo=ZoneInfo("Asia/Tehran")),
    chat_id=chat_id,
    name=name
        )
    print("JOB:", job)
    
    keyboard = [
        ["ثبت یادآوری","لیست یادآوری ها"],
        ["تنظیمات"],["/start"]
    ]

    # for buttons
    reply_keyboard = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard = True
    )

    
    
    user = update.effective_user   # To display the username
    await update.message.reply_text(f"سلام {user.first_name}",reply_markup=reply_keyboard)

app = Application.builder().token(TOKEN).post_init(post_init).build()
app.add_handler(CommandHandler("start",start))

app.run_polling()