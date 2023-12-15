from aiogram.types import Message

from src.routers.default.router import default_router
from src.utils.lexicon import OTHER_MESSAGE


@default_router.message()
async def process_other_messages(message: Message) -> None:
    await message.answer(text=OTHER_MESSAGE)
