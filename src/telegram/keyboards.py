from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="❔ Гайд", callback_data="guide_button"),
            InlineKeyboardButton(text="🔮 Гитхаб", callback_data="github_button", url="https://github.com/Vealke/ACHY-Plus")
        ],
        [
            InlineKeyboardButton(text="☑️ Начать", callback_data="start_button")
        ]
    ]
)

bot_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Запустить", callback_data="turnon_button")
        ],
        [
            InlineKeyboardButton(text="❌ Отключить", callback_data="turnoff_button")
        ]
    ]
)