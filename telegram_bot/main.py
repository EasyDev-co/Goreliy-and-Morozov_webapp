from loader import dp
from aiogram import executor
from loguru import logger
from handlers import start


@dp.message_handler()
async def pass_handler(message):
    pass


if __name__ == '__main__':
    logger.info("--BOT IS STARTING--")
    executor.start_polling(dp, skip_updates=True)
