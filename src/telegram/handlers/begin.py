import os
import asyncio

from typing import List
from dotenv import load_dotenv

from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode
from aiogram import Router, F, Bot

router = Router()

load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = Bot(TOKEN)

garbage: List[int] = []
response: List[str] = []

async def checkout(data: List[int],
                   ctd: int) -> bool:

    print(data)
    print(len(response))
    
    await asyncio.sleep(5)
    match len(response):
        case 5:
            await bot.delete_messages(ctd, data)
            return True
        case _:
            await checkout(garbage, ctd)

class Schema(StatesGroup):
    nickname: str = State()
    password: str = State()
    second_nickname: str = State()
    anarchy_team: int = State()
    anarchy_number: int = State()
    ensurence: str = State()

@router.callback_query(F.data == "start_button")
async def function(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.set_state(Schema.nickname)
    new_message = await call.message.answer("✨ <b>УСТАНОВКА</b>\n\n" \
                                            "Пожалуйста, укажите имя аккаунта для бота.", 
                                            parse_mode=ParseMode.HTML)
    chat_id = new_message.chat.id
    garbage.append(new_message.message_id)

    t1 = asyncio.create_task(checkout(data=garbage, ctd=chat_id))
    asyncio.gather(t1)

@router.message(Schema.nickname)
async def function(message: Message, state: FSMContext):
    await state.set_state(Schema.password)
    await state.update_data(bot=message.text)
    new_message = await message.answer("✨ <b>УСТАНОВКА</b>\n\n" \
                                       "Пожалуйста, укажите пароль аккаунта от бота.", 
                                       parse_mode=ParseMode.HTML)
    print(type(message.from_user.id))
    print(message.from_user.id)
    garbage.extend([new_message.message_id, message.message_id])

@router.message(Schema.password)
async def function(message: Message, state: FSMContext):
    await state.set_state(Schema.second_nickname)
    await state.update_data(pw=message.text)

    bot_data = await state.get_data()
    bot_name = bot_data.get("bot")

    new_message = await message.answer("✨ <b>УСТАНОВКА</b>\n\n" \
                                       f"Пожалуйста, укажите ваш ник для того, что бы <b>{bot_name}</b> мог отправить вам тп запрос.", 
                                       parse_mode=ParseMode.HTML)
    garbage.extend([new_message.message_id, message.message_id])

@router.message(Schema.second_nickname)
async def function(message: Message, state: FSMContext):
    await state.set_state(Schema.anarchy_team)
    await state.update_data(user=message.text)

    kb = InlineKeyboardBuilder()

    types = ["1x", "2x", "3x",
             "5x", "10x"]
    
    for item in types:
        kb.button(text=f"{item}", callback_data=f"{item}")
    types_keyboard = kb.adjust(3, 3).as_markup()

    new_message = await message.answer("✨ <b>УСТАНОВКА</b>\n\n" \
                                       f"Выберите тип режима:\n\n*<b>Сколько человек в команде</b>", 
                                       parse_mode=ParseMode.HTML,
                                       reply_markup=types_keyboard)
    
    garbage.extend([new_message.message_id, message.message_id])

@router.callback_query(Schema.anarchy_team)
async def function(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.set_state(Schema.anarchy_number)
    await state.update_data(serv_type=call.data)

    #TODO: На будущее если пользователь будет вводить 3-х значное число, убирать от него первую цифру

    new_message = await call.message.answer("✨ <b>УСТАНОВКА</b>\n\n" \
                                            f"Введите номер анархии:\n\n", 
                                            parse_mode=ParseMode.HTML)
    
    garbage.extend([new_message.message_id, call.message.message_id])

@router.message(Schema.anarchy_number)
async def function(message: Message, state: FSMContext):
    await state.set_state(Schema.ensurence)
    await state.update_data(serv_num=message.text)
    
    garbage.append(message.message_id)

    data = await state.get_data()
    response.extend([data.get("user"), data.get("pw"), data.get("bot"),
                     data.get("serv_type"), data.get("serv_num") ])