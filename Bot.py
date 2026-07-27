from flask import Flask
from threading import Thread
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN
from handlers import start, message_handler
web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "Bot is running"

def run_server():
    web_app.run(host="0.0.0.0", port=10000)

def keep_alive():
    Thread(target=run_server).start()
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Командаи /start
    app.add_handler(CommandHandler("start", start))

    # Коркарди паёмҳои матнӣ
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler)
    )

    print("Бот фаъол шуд...")
    app.run_polling()

if __name__ == "__main__":
    main()
