from flask import Flask, request
from threading import Thread

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN
from handlers import start, message_handler


web_app = Flask(__name__)

application = Application.builder().token(BOT_TOKEN).build()


@web_app.route("/")
def home():
    return "Bot is running"


@web_app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(
        request.get_json(force=True),
        application.bot
    )

    application.update_queue.put_nowait(update)

    return "OK"


def run_server():
    web_app.run(
        host="0.0.0.0",
        port=10000
    )


def main():
    application.add_handler(
        CommandHandler("start", start)
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            message_handler
        )
    )

    Thread(target=run_server).start()

    application.run_webhook(
        listen="0.0.0.0",
        port=10000,
        webhook_url="https://НОМИ-SERVICE-И-RENDER.onrender.com/webhook"
    )


if __name__ == "__main__":
    main()
