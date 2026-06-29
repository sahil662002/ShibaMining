from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def join_channel():
    keyboard = [
        [InlineKeyboardButton("📢 Join Channel", url="https://t.me/ShibaMiningOfficial")],
        [InlineKeyboardButton("✅ Verify Join", callback_data="verify_join")]
    ]

    return InlineKeyboardMarkup(keyboard)
