from telegram_bot.loader import dp
from aiogram import executor


@dp.message_handler()
async def pass_handler(message):
    pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
