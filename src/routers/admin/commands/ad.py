from aiogram.filters.command import Command
from aiogram.filters.state import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message

from src.common.fsm.ad_filling_state import FSMAdFillForm
from src.routers.admin.router import admin_router
from src.utils.lexicon import ENTER_AD_TEXT_MESSAGE


@admin_router.message(
    StateFilter(default_state),
    Command(commands='ad')
)
async def process_ad_command(
        message: Message,
        state: FSMContext
) -> None:
    await message.answer(text=ENTER_AD_TEXT_MESSAGE)
    await state.set_state(FSMAdFillForm.fill_ad_text)
