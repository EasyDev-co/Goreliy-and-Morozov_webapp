from aiogram import types

from loader import dp
from keyboards.web_app import get_menu_web_app, get_menu_button
from loader import bot


@dp.message_handler(commands=['start'])
async def message_handler(message: types.Message):
    await message.answer("some_text", reply_markup=get_menu_button())
    await bot.set_chat_menu_button(
        chat_id=message.chat.id,
        menu_button=get_menu_web_app()
    )
