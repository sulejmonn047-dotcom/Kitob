# keyboards.py
from telegram import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton("📚 Китобҳо")],
        [KeyboardButton("💰 Нархнома")],
        [KeyboardButton("💳 Пардохт")],
        [KeyboardButton("📞 Тамос бо админ")]
    ],
    resize_keyboard=True
)
