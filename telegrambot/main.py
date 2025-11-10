import asyncio
import logging
from aiogram import Dispatcher, Bot
from telegrambot.config import TOKEN

dp = Dispatcher()
bot = Bot(token=TOKEN)


async def main_polling():
    dp.include_routers()
    await dp.start_polling(bot)


if __name__ == '__main__':
        try:
            asyncio.run(main_polling())
        except (KeyboardInterrupt, SystemExit):
            logging.error("Бот выключен!")