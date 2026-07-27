# handlers.py
from telegram import Update
from telegram.ext import ContextTypes

ADMIN_USERNAME = "@kitobi_dustdoshta"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 Ба боти фурӯши китобҳо хуш омадед!\n\n"
        "Аз меню интихоб кунед 👇"
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text == "📚 Китобҳо":
        await update.message.reply_text(
            "📚 Рӯйхати китобҳо:\n\n"
            "1️⃣ Китоби оддӣ — 10 сомонӣ\n"
            "2️⃣ 2 китоб — 15 сомонӣ\n"
            "3️⃣ 6 китоби Саймурод Давлатов — 45 сомонӣ\n\n"
            "Барои харид ба админ нависед."
        )

    elif text == "📞 Тамос бо админ":
        await update.message.reply_text(
            f"📩 Барои тамос бо админ:\n\n"
            f"{ADMIN_USERNAME}\n\n"
            "Савол ё фармоиши худро нависед."
        )

    elif text == "💳 Нархҳо":
        await update.message.reply_text(
            "💰 Нархҳо:\n\n"
            "📖 1 китоб — 10 сомонӣ\n"
            "📚 2 китоб — 15 сомонӣ\n"
            "📚 6 китоби Саймурод Давлатов — 45 сомонӣ\n"
            "📚 Ҳамаи 24 китоб — 180 сомонӣ"
        )

    else:
        await update.message.reply_text(
            "Лутфан аз меню интихоб кунед 👇"
        )
