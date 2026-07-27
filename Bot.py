from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from Config import BOT_TOKEN
from handlers import start, message_handler

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
