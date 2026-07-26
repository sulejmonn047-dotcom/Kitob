from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8716435321:AAGokhQ-JKLOHdDQbp1DEWYlorgHwPnhI_s"

keyboard = [
    ["📚 Китобҳо"],
    ["💰 Нархнома"],echo "# Kitob" >> README.md 
git init 
git add README.md 
git commit -m "first commit" 
git branch -M main 
git remote add origin https://github.com/sulejmonn047-dotcom/Kitob.git
 git push -u origin main
    ["📞 Тамос"]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Хуш омадед ба боти фурӯши китоб!",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📚 Китобҳо":
        await update.message.reply_text(
            "📖 Китобҳо:\n"
            "1. Як китоб — 10 сомонӣ\n"
            "2. Ду китоб — 15 сомонӣ\n"
            "3. 6 китоби Саидмурод Давлатов — 50 сомонӣ\n"
            "4. Ҳамаи 24 китоб — 180 сомонӣ"
        )

    elif text == "💰 Нархнома":
        await update.message.reply_text(
            "💰 Нархнома:\n"
            "• 1 китоб — 10 сомонӣ\n"
            "• 2 китоб — 15 сомонӣ\n"
            "• 6 китоб — 50 сомонӣ\n"
            "• 24 китоб — 180 сомонӣ"
        )

    elif text == "📞 Тамос":
        await update.message.reply_text(
            "Барои харид ба администратор нависед."
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu))

print("Bot started...")
app.run_polling()
bot.infinity_polling()
