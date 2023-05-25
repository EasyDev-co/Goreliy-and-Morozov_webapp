from aiogram import types

from telegram_bot.loader import dp
from telegram_bot.keyboards.web_app import web_app_button, get_menu_button
from telegram_bot.loader import bot


@dp.message_handler(commands=['start'])
async def message_handler(message: types.Message):
    await message.answer("some_text", reply_markup=web_app_button)
    await bot.set_chat_menu_button(
        chat_id=message.chat.id,
        menu_button=get_menu_button()
    )
