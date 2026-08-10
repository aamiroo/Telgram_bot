# Telegram Reminder Bot

A simple Telegram reminder bot written in Python using the **python-telegram-bot** library.

**Bot:** `@Reminder_amir_bot`

## Features

* Welcome users with `/start`
* Custom keyboard buttons
* Register users in SQLite
* Create daily reminders
* Send reminder messages at a specified time
* Restore reminders when the bot starts

## Requirements

* Python 3.10+
* [uv](https://docs.astral.sh/uv/)
* SQLite
* Telegram Bot Token

## Install uv

Install `uv` with:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After installation, restart your terminal or reload your shell.

Check the installation:

```bash
uv --version
```

## Install Dependencies

This project uses **uv** for Python environment and dependency management.

Install the project dependencies with:

```bash
uv sync
```

## Configuration

Create a `.env` file in the project directory:

```env
TOKEN=your_telegram_bot_token
```

Replace `your_telegram_bot_token` with your Telegram bot token.

> **Important:** Do not upload the `.env` file to GitHub.

## Database

The bot uses **SQLite** to store registered users.

The database is automatically created when the bot starts:

```text
chatid.db
```

Database operations are handled by the `Database` class in:

```text
database.py
```

The database contains a `users` table with:

```text
id
chat_id
```

## Run

Run the bot using `uv`:

```bash
uv run python3 reminder_bot.py
```

## Project Structure

```text
telegram_bot/
├── database.py
├── reminder_bot.py
├── README.md
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
└── src/
```

## Future Improvements

* Delete reminders
* Edit reminders
* Multiple reminders per user
* Daily and weekly reminders
* Reminder settings
* MySQL support
* Metabase integration
