"""
this bot in telegram with id @Reminder_amir_bot .
This bot is designed to send daily reminders.
"""
# Using the Telegram Bot Library
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters,
    ConversationHandler,
)
from datetime import time   # To send an automated reminder at a specific time
from zoneinfo import ZoneInfo   # To determine the location for the clock



# Obtaining a token from BotFather
TOKEN = "8736640642:AAGe7DtH6wJGOWz3LhlixJzJ5R_o0tTurZ0"

TEXT, TIME = range(2)

# reminder function for auto reminder in bot
async def reminder (context : ContextTypes.DEFAULT_TYPE):
    chat_id = context.job.chat_id
    await context.bot.send_message(
        chat_id = chat_id ,
        text = "وقتش رسید"
    )
# Start function for /start in bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # async 
    keyboard = [
        ["ثبت یادآوری","لیست یادآوری ها"],
        ["تنظیمات"],["/start"]
    ]

    # for buttons
    reply_keyboard = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard = True
    )

    
    chat_id = update.effective_chat.id
    print("job created", chat_id)
    context.job_queue.run_daily(
        reminder,
        time=time(hour=11, minute=47 , tzinfo=ZoneInfo("Asia/Tehran")),
        chat_id=chat_id
    )
    user = update.effective_user   # To display the username
    await update.message.reply_text(f"سلام {user.first_name}",reply_markup=reply_keyboard)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start",start))

app.run_polling()