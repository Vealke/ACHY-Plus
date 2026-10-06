import os
import asyncio

from dotenv import load_dotenv

from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery
from aiogram.enums import ParseMode

from src.telegram.keyboards import bot_kb

load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = Bot(TOKEN)

router = Router()

@router.callback_query(F.data == "turnon_button")
async def start_func(call: CallbackQuery):

    await call.answer()

    bot_message = await call.message.reply("✅ <b>Бот включен!</b>",
                                            parse_mode=ParseMode.HTML)
    message_id = bot_message.message_id
    chat_id = bot_message.chat.id

    await asyncio.sleep(3)

    await bot.delete_message(message_id=message_id,
                             chat_id=chat_id)

@router.callback_query(F.data == "turnoff_button")
async def start_func(call: CallbackQuery):

    await call.answer()

    bot_message = await call.message.reply("❌ <b>Бот выключен!</b>",
                                            parse_mode=ParseMode.HTML)
    message_id = bot_message.message_id
    chat_id = bot_message.chat.id

    await asyncio.sleep(3)

    await bot.delete_message(message_id=message_id,
                             chat_id=chat_id)