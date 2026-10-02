from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message
from cachetools import TTLCache

#TODO: Или я тупой или эта хуйня кривая, её пофиксить надо будет.

class ThrottlingMiddleware(BaseMiddleware):
    """
    Инициализация middleware.
        param time_limit (float): 
        Время в секундах, после которого повторный запрос будет заблокирован.
    """
    def __init__(self, time_limit: float = 2.5) -> None:
        super().__init__()
        self.cache = TTLCache(maxsize=10_000, ttl=time_limit)

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        # Проверяем, что событие является сообщением (Message)
        if isinstance(event, Message) and event.from_user:
            user_id = event.from_user.id

            # Если пользователь уже есть в кэше — игнорируем его сообщение
            if user_id in self.cache:
                await event.answer("Слишком часто! Подождите немного.")
                return 

            self.cache[user_id] = True

        return await handler(event, data)