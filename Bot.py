from flask import Flask, request
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN
from handlers import start, message_handler


app = Flask(__name__)

application = Application.builder().token(BOT_TOKEN).build()


@app.route("/")
def home():
    return "Bot is running"


@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(
        request.get_json(force=True),
        application.bot
    )

    application.update_queue.put_nowait(update)
    return "OK"


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

    application.initialize()
    application.start()

    # Webhook барои Render
    application.bot.set_webhook(
        "https://kitob-3.onrender.com/webhook"
    )

    app.run(
        host="0.0.0.0",
        port=10000
    )


if __name__ == "__main__":
    main()
