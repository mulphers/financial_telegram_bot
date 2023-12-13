import asyncio

from aiogram import Bot, Dispatcher

from src.common.keyboards.command_menu import set_command_menu
from src.core.settings import load_settings
from src.routers import router


async def main() -> None:
    settings = load_settings()

    bot = Bot(token=settings.bot.token)
    dp = Dispatcher()

    dp.include_router(router)

    await set_command_menu(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
