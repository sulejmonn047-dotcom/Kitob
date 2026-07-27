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
    book_list = "📚 Рӯйхати китобҳо:\n\n"

    for book in BOOKS:
        book_list += f"{book['id']}. {book['name']}\n"

    await update.message.reply_text(book_list)

    elif text == "💰 Нархнома":
        await update.message.reply_text(
            "1 китоб — 10 сомонӣ\n"
            "2 китоб — 15 сомонӣ\n"
            "6 китоби Саидмурод Давлатов — 45 сомонӣ\n"
            "Ҳамаи 24 китоб —? сомонӣ"
        )

    elif text == "💳 Пардохт":
        await update.message.reply_text(
            "Корти пардохт:\n"
            "5058 2701 1508 5556"
        )

    elif text == "📞 Тамос":
        await update.message.reply_text(
            "Барои тамос ба админ нависед."
        )
