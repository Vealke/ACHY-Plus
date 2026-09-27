__all__ = ("router")

from aiogram import Router

from src.telegram.handlers import start
from src.telegram.handlers import guide

router = Router()

router.include_routers(
    start.router,
    guide.router
    )