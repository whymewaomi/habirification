import asyncio
import logging
from aiogram import Dispatcher, Bot
from telegrambot.config import TOKEN
from telegrambot.heandler.start import startbot

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создаём объекты бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    # Подключаем роутеры
    dp.include_router(startbot)

    print("🚀 Бот запущен!")
    # Запускаем процесс polling
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("🛑 Бот остановлен!")
