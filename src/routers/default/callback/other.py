from aiogram.types import CallbackQuery

from src.routers.default.router import default_router
from src.utils.lexicon import STATE_WARNING_MESSAGE


@default_router.callback_query()
async def process_callback_in_state(callback: CallbackQuery):
    await callback.answer(text=STATE_WARNING_MESSAGE)
