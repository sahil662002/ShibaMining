from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

from config import BOT_TOKEN
from database import create_tables, add_user, is_verified
from keyboards.join_channel import join_channel
from keyboards.webapp_menu import webapp_menu
from handlers.verify_join import verify_join


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    add_user(user.id, user.username, user.first_name)

    if is_verified(user.id):

        await update.message.reply_text(
            f"🏠 Welcome Back {user.first_name}!\n\n"
            "✅ Your account is verified successfully.\n\n"
            "👇 Click the button below to open the Shiba Mining App.",
            reply_markup=webapp_menu()
        )

    else:

        await update.message.reply_text(
            "👋 Welcome to Shiba Mining Bot!\n\n"
            "To continue using this bot, please join our official Telegram channel first.\n\n"
            "After joining, click the ✅ Verify Join button.",
            reply_markup=join_channel()
        )


def main():
    create_tables()

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        CallbackQueryHandler(
            verify_join,
            pattern="verify_join"
        )
    )

    print("✅ Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
