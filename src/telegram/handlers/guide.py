from aiogram import Router, F

from aiogram.types import CallbackQuery
from aiogram.enums.parse_mode import ParseMode

from src.telegram.keyboards import start_kb

router = Router()

guide_message: str = "1️⃣ <b>Создайте новый майнкрафт аккаунт, со свободным ником через используемый вами лаунчер.</b>\n\n" \
                     "2️⃣ <b>Войдите с созданного аккаунта на сервер и пройдите капчу, зарегистрируйтесь.</b>\n\n" \
                     "3️⃣ <b>Возьмите и запишите/запомните координаты безопасного места, куда может встать бот.</b>\n\n" \
                     '4️⃣ <b>Зайдите в нашего тг-бота и нажмите "☑️ Начать", после чего заполните данные и пользуйтесь.</b>\n\n' \
                     "<b>В момент запуска бота, вы должны находиться на сервере с аккаунта, который уже находится на базе. В течение 3-х </b>" \
                     "<b> минут вам придёт запрос на тп от бота, который нужно принять на координатах которые вы запомнили раннее.</b>"

@router.callback_query(F.data == "guide_button")
async def start_func(call: CallbackQuery):
    await call.answer()
    await call.message.reply(guide_message, 
                             reply_markup=start_kb,
                             parse_mode=ParseMode.HTML)
