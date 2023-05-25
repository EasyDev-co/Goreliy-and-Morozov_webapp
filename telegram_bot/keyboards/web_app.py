from aiogram import types

from telegram_bot.core.config import settings

web_app_button = types.InlineKeyboardMarkup().add(
    types.InlineKeyboardButton(
        text="Open",
        web_app=settings.WEB_APP_URL
    )
)


def get_menu_button():
    web_app = types.WebAppInfo(url=f"{settings.WEB_APP_URL}")
    web_app_inline_keyboard = types.InlineKeyboardButton(
        text="Начать",
        web_app=web_app
    )
    return types.InlineKeyboardMarkup().add(web_app_inline_keyboard)
