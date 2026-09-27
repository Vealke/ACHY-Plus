
# 1. Переход в панель бота по команде /start
# 2. Меню будет содержать кнопки:
#   I - Туториал; II - Гитхаб
#       III - Начать;
# 3. Система будет следующая: пользователь сам создаёт бот аккаунт в майнкрафт, один раз входит в него перед использованием бота, после чего,
#    нужно поочерёдно отправить в бота ник бот-аккаунта, пароль от него и координаты где он должен встать.
# 4. Бот занимает позицию и начинает тречить окружающих сущностей

import os
import asyncio
import logging

from rich.console import Console
from aiogram import Dispatcher, Bot
from dotenv import load_dotenv

from src import router as main_router

load_dotenv()
console = Console()
TOKEN = os.getenv("TOKEN")

async def main():

    logging.info("The bot just has started")

    bot = Bot(TOKEN)
    dp = Dispatcher()

    # ts is important ↓
    # dp["db_pool"] = localSession

    dp.include_router(main_router)

    console.print(f"[bold green]BOT ID: {bot.id}\n" \
                  f"BOT TOKEN: {TOKEN}[bold green]\n" \
                   "The bot is now ready to use!") 

    await bot.delete_webhook(True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())