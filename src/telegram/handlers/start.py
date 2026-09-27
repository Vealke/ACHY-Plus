from aiogram import Router, F

from aiogram.types import Message
from aiogram.filters import CommandStart

from src.telegram.keyboards import start_kb

router = Router()

@router.message(CommandStart())
async def start_func(message: Message):
    await message.reply("Боишься что твою кибитку снесут нахуй пока ты спишь?\nТебе к нам! 😉😏", reply_markup=start_kb)