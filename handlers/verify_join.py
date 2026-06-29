from telegram import Update
from telegram.ext import ContextTypes

from config import CHANNEL_USERNAME
from database import verify_user


async def verify_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id

    try:
        member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)

        if member.status in ["member", "administrator", "creator"]:
            verify_user(user_id)

            await query.message.reply_text(
                "🎉 Congratulations!\n\n"
                "✅ Channel verification completed successfully.\n"
                "🚀 Your account has been activated."
            )

        else:
            await query.answer(
                "❌ Please join our channel first.",
                show_alert=True
            )

    except Exception:
        await query.answer(
            "❌ Please join our channel first.",
            show_alert=True
        )
