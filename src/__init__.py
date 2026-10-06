__all__ = ("router")

from aiogram import Router

from src.telegram.handlers import start
from src.telegram.handlers import guide
from src.telegram.handlers import begin

from src.telegram.handlers.control import bot_panel

router = Router()

router.include_routers(
    start.router,
    guide.router,
    begin.router,
    bot_panel.router
    )