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
    text = update.message.text.lower()

    if text == "📚 китобҳо":
        books_text = "📖 Рӯйхати китобҳо:\n\n"

        for book in BOOKS:
            books_text += (
                f"🔹 {book['id']}. {book['name']}\n"
                f"💰 Нарх: {book['price']} сомонӣ\n\n"
            )

        books_text += "📌 Барои маълумоти китоб рақами онро нависед (мисол: 5)"
        await update.message.reply_text(books_text)


    elif text == "📞 тамос бо админ":
        await update.message.reply_text(
            "✍️ Барои тамос бо админ нависед:\n@kitobi_dustdoshta"
        )


    elif text == "💰 нархнома":
        await update.message.reply_text(
            "💰 Нархнома ва аксия:\n\n"
            "🔥 Аксия:\n"
            "📚 23 китоб — ҳамагӣ 70 сомонӣ\n\n"
            "📖 Китобҳои Саймурод Давлатов — 25 сомонӣ"
        )

           await update.message.reply_text(
    f"Барои пардохт ба карта гузаронед:\n\n{CARD_NUMBER}"
)


    elif text.isdigit():
        book_id = int(text)

        for book in BOOKS:
            if book["id"] == book_id:
                await update.message.reply_text(
                    f"📖 {book['name']}\n\n"
                    f"💰 Нарх: {book['price']} сомонӣ\n\n"
                    f"📝 Шарҳ:\n{book['description']}"
                )
                return

        await update.message.reply_text(
            "❌ Чунин рақами китоб ёфт нашуд."
        )


    elif "саймурод" in text:
        await update.message.reply_text(
            "📚 Саймурод Давлатов муаллифи китобҳои рушди шахсӣ ва молиявӣ мебошад.\n\n"
            "📖 Китобҳои ӯ дар бот бо аксия 25 сомонӣ мебошанд."
        )


    elif "бой" in text:
        await update.message.reply_text(
            "💡 Барои рушди молиявӣ тавсия:\n\n"
            "📘 Дилхоҳ шахс метавонад бой шавад\n"
            "📘 Фикр кун ва бой шав\n"
            "📘 Падари фақир ва сарватманд"
        )


    elif "кадом китоб" in text or "китоби хуб" in text:
        await update.message.reply_text(
            "⭐ Тавсияҳо:\n\n"
            "🚀 Барои одатҳо:\n📗 Одатҳои атомӣ\n\n"
            "💰 Барои пул:\n📘 Фикр кун ва бой шав\n"
            "📘 Бойтарин одам дар Бобил\n\n"
            "🧠 Барои рушди шахсӣ:\n📙 Китобҳои Саймурод Давлатов"
        )


    elif "китоб" in text and any(char.isdigit() for char in text):
        number = ''.join(filter(str.isdigit, text))
        book_id = int(number)

        for book in BOOKS:
            if book["id"] == book_id:
                await update.message.reply_text(
                    f"📖 {book['name']}\n\n"
                    f"📝 {book['description']}\n\n"
                    f"💰 Нарх: {book['price']} сомонӣ"
                )
                return


    else:
        await update.message.reply_text(
            "🤖 Саволи худро нависед.\n\n"
            "Мисол:\n"
            "• Саймурод Давлатов кист?\n"
            "• Кадом китоб бихонам?\n"
            "• Китоби 5-ро нишон деҳ",
            reply_markup=main_keyboard
        )
