import logging
import os
import subprocess

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logger = logging.getLogger(__name__)

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

ALLOWED_USERS = [int(id) for id in os.getenv("ALLOWED_USERS").split(",")]


async def check_user(update: Update) -> bool:
    if update.effective_user.id not in ALLOWED_USERS:
        await update.message.reply_text("You are not allowed to use this bot")
        return False
    return True


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"Hello {update.effective_user.first_name} - {update.effective_user.id}! \n Commands available: \n /check"
    )


async def check_schiuma(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not await check_user(update):
        return

    await update.message.reply_text("Checking for Schiuma")
    subprocess.run(["docker", "compose", "up"])
    print("done")
    await update.message.reply_text("Checked")


def run():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("check", check_schiuma))
    app.run_polling()


if __name__ == "__main__":
    # run()
    print(TOKEN)
    print(ALLOWED_USERS)
    # subprocess.run(["docker", "compose", "up"])
