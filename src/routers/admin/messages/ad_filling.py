from aiogram import Bot, F
from aiogram.filters.state import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, PhotoSize

from src.common.fsm.ad_filling_state import FSMAdFillForm
from src.routers.admin.router import admin_router
from src.utils.lexicon import (END_AD_MESSAGE, ENTER_BUTTON_TEXT_MESSAGE,
                               ENTER_PHOTO_MESSAGE, ENTER_URL_MESSAGE,
                               START_AD_MESSAGE, WARNING_DATA_SEND_MESSAGE)
from src.utils.send_ad import send_ad_all_active_users


@admin_router.message(
    StateFilter(FSMAdFillForm.fill_ad_text),
    F.text
)
async def process_ad_text_send(
        message: Message,
        state: FSMContext
) -> None:
    await state.update_data(ad_text=message.text)
    await message.answer(text=ENTER_PHOTO_MESSAGE)
    await state.set_state(FSMAdFillForm.upload_photo)


@admin_router.message(
    StateFilter(FSMAdFillForm.upload_photo),
    F.photo[-1].as_('photo')
)
async def process_upload_photo(
        message: Message,
        photo: PhotoSize,
        state: FSMContext
) -> None:
    await state.update_data(photo=photo.file_id)
    await message.answer(text=ENTER_BUTTON_TEXT_MESSAGE)
    await state.set_state(FSMAdFillForm.fill_button_text)


@admin_router.message(
    StateFilter(FSMAdFillForm.fill_button_text),
    F.text
)
async def process_button_text_send(
        message: Message,
        state: FSMContext
) -> None:
    await state.update_data(button_text=message.text)
    await message.answer(text=ENTER_URL_MESSAGE)
    await state.set_state(FSMAdFillForm.fill_url)


@admin_router.message(
    StateFilter(FSMAdFillForm.fill_url),
    F.text
)
async def process_url_send(
        message: Message,
        bot: Bot,
        state: FSMContext
) -> None:
    await state.update_data(url=message.text)
    data = await state.get_data()
    await state.clear()

    await message.answer(text=START_AD_MESSAGE)
    await send_ad_all_active_users(  # type: ignore[call-arg]
        bot=bot,
        data=data
    )
    await message.answer(text=END_AD_MESSAGE)


@admin_router.message(StateFilter(FSMAdFillForm))
async def warning_data_send(message: Message) -> None:
    await message.answer(text=WARNING_DATA_SEND_MESSAGE)
