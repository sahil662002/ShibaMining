from telegram import ReplyKeyboardMarkup


def main_menu():
    keyboard = [
        ["⛏ Start Mining", "🎮 Games"],
        ["💰 Wallet", "👥 Referral"],
        ["💸 Withdraw", "📺 Watch Ads"],
        ["📢 Join Channel", "ℹ️ Help"]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )
