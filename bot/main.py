import asyncio

from aiogram import Bot, Dispatcher

from .config import load_bot_token
from .handlers import router


async def main() -> None:
    token = load_bot_token()
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
