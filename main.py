import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("👑 شاه", callback_data="شاه")],
        [InlineKeyboardButton("🏛 رئیس‌جمهور", callback_data="رئیس‌جمهور")],
        [InlineKeyboardButton("⚜️ رهبر", callback_data="رهبر")],
        [InlineKeyboardButton("🎖 فرمانده", callback_data="فرمانده")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🌍 به Sunleon خوش آمدید!\n\n"
        "لطفاً انتخاب کنید دوست دارید چگونه خطاب شوید.",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    title = query.data

    await query.edit_message_text(
        f"✅ از این پس شما با عنوان «{title}» خطاب خواهید شد."
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
