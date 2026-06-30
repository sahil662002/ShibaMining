from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo


def webapp_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "🚀 Open Shiba Mining App",
                web_app=WebAppInfo(
                    url="https://shibamining.pages.dev"
                )
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)
