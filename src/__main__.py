import asyncio

from aiogram import Bot, Dispatcher
from fast_depends import dependency_provider

from src.common.keyboards.command_menu import set_command_menu
from src.common.markers.gateway import TransactionGatewayMarker
from src.core.settings import load_settings
from src.database.core.connection import (create_as_engine,
                                          create_as_session_factory)
from src.database.core.gateway import TransactionGateway
from src.routers import router


async def main() -> None:
    settings = load_settings()

    async_engine = create_as_engine(url=settings.db.url)
    async_session_factory = create_as_session_factory(engine=async_engine)

    dependency_provider.override(TransactionGatewayMarker, TransactionGateway(async_session_factory()))

    bot = Bot(token=settings.bot.token)
    dp = Dispatcher()

    dp.include_router(router=router)

    await set_command_menu(bot=bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
