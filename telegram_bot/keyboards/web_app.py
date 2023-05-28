from aiogram import types

from core.config import settings


def get_menu_web_app():
    web_app = types.WebAppInfo(url=f"{settings.WEB_APP_URL}")
    return types.MenuButtonWebApp(text="Начать", web_app=web_app)


def get_menu_button():
    web_app = types.WebAppInfo(url=f"{settings.WEB_APP_URL}")
    web_app_inline_keyboard = types.InlineKeyboardButton(
        text="Начать",
        web_app=web_app
    )
    return types.InlineKeyboardMarkup().add(web_app_inline_keyboard)
