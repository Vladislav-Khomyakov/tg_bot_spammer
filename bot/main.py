import asyncio

from aiogram import Bot, Dispatcher

from .config import load_bot_token
from .handlers import router


async def main() -> None:
    token = load_bot_token()
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router)

    # Ensure polling works even if a webhook was previously set
    await bot.delete_webhook(drop_pending_updates=True)

    # Poll only for update types used by registered handlers
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
