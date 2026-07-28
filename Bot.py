import asyncio
import threading

from flask import Flask

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN
from handlers import start, message_handler


# Flask барои Render
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Bot is running"


def run_flask():
    flask_app.run(
        host="0.0.0.0",
        port=10000
    )


async def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            message_handler
        )
    )

    print("Bot started...")

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    await asyncio.Event().wait()


if __name__ == "__main__":
    threading.Thread(
        target=run_flask,
        daemon=True
    ).start()

    asyncio.run(main())
