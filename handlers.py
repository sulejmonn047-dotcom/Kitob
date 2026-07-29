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

        books_text += "📌 Барои дидани маълумоти китоб рақами онро нависед."
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

    elif text.isdigit():
        book_id = int(text)

        for book in BOOKS:
            if book["id"] == book_id:
                await update.message.reply_text(
                    f"📖 {book['name']}\n\n"
                    f"💰 Нарх: {book['price']} сомонӣ\n\n"
                    f"{book['description']}"
                )
                return

        await update.message.reply_text(
            "❌ Чунин рақами китоб ёфт нашуд."
        )

    elif "саймурод" in text.lower():
        await update.message.reply_text(
            "📚 Саймурод Давлатов муаллифи китобҳои рушди шахсӣ ва молиявӣ мебошад.\n"
            "📖 Китобҳои ӯ дар бот бо аксия 25 сомонӣ мебошанд."
        )

    elif "бой" in text.lower():
        await update.message.reply_text(
            "💡 Барои рушди молиявӣ ин китобҳоро тавсия медиҳам:\n\n"
            "📘 Дилхоҳ шахс метавонад бой шавад\n"
            "📘 Фикр кун ва бой шав\n"
            "📘 Падари фақир ва сарватманд"
        )

    elif "китоби хуб" in text.lower() or "кадом китоб" in text.lower():
        await update.message.reply_text(
            "⭐ Тавсияҳо:\n\n"
            "🚀 Барои одатҳо:\n📗 Одатҳои атомӣ\n\n"
            "💰 Барои пул ва молия:\n📘 Фикр кун ва бой шав\n"
            "📘 Бойтарин одам дар Бобил\n\n"
            "🧠 Барои рушди шахсӣ:\n📙 Китобҳои Саймурод Давлатов"
        )

    else:
        await update.message.reply_text(
            "🤖 Саволи худро нависед.\n\n"
            "Масалан:\n"
            "• Саймурод Давлатов кист?\n"
            "• Кадом китоб бихонам?\n"
            "• Китоби 5-ро нишон деҳ"
        ) 
