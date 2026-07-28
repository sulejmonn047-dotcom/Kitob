# handlers.py
from books import BOOKS
from telegram import Update
from telegram.ext import ContextTypes
from keyboards import main_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 Ба боти фурӯши китобҳо хуш омадед!",
        reply_markup=main_keyboard
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📚 Китобҳо":
        books_text = "📖 Рӯйхати китобҳо:\n\n"

        for book in BOOKS:
            books_text += (
                f"🔹 {book['id']}. {book['name']}\n"
                f"💰 Нарх: {book['price']} сомонӣ\n\n"
            )

        await update.message.reply_text(books_text)

    elif text == "📞 Тамос бо админ":
        await update.message.reply_text(
            "✍️ Барои тамос бо админ нависед:\n@kitobi_dustdoshta"
        )

    elif text == "💰 Нархнома":
        await update.message.reply_text(
            "💰 Нархнома ва аксия:\n\n"
            "🔥 Аксия:\n"
            "📚 23 китоб — ҳамагӣ 70 сомонӣ\n\n"
            "📖 Китобҳои Саймурод Давлатов — 25 сомонӣ"
        )

    elif text == "💳 Пардохт":
        await update.message.reply_text(
            "💳 Барои пардохт ба админ нависед:\n@kitobi_dustdoshta"
        )

    else:
        await update.message.reply_text(
            "Лутфан аз меню интихоб кунед 📋",
            reply_markup=main_keyboard
        )
