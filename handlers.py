# handlers.py
from telegram import Update
from telegram.ext import ContextTypes
from books import BOOKS
from keyboards import main_keyboard


ADMIN_USERNAME = "@username_admin"  # номи админро инҷо мон


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 Ба боти фурӯши китобҳо хуш омадед!",
        reply_markup=main_keyboard
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📞 Тамос бо админ":
        await update.message.reply_text(
            f"📩 Барои тамос бо админ:\n\n{ADMIN_USERNAME}\n\n"
            "Савол ё дархости худро нависед."
        )

    elif text == "📚 Китобҳо":
        text_books = "📚 Рӯйхати китобҳо:\n\n"

        for book in BOOKS:
            text_books += f"📖 {book['id']}. {book['name']} - {book['price']} сомонӣ\n"

        await update.message.reply_text(text_books)

    else:
        await update.message.reply_text(
            "Лутфан аз меню интихоб кунед 👇",
            reply_markup=main_keyboard
        )
