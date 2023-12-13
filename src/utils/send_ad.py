from aiogram import Bot

from src.common.interfaces.abstract_uow import AbstractUnitOfWork
from src.common.keyboards.keyboard_generator import generate_ad_keyboard
from src.utils.decorators import with_database


@with_database
async def send_ad_all_active_users(
        bot: Bot,
        data: dict[str, str],
        uow: AbstractUnitOfWork
):
    for user in await uow.user.get_list_active_user():
        await bot.send_photo(
            chat_id=user.user_id,
            photo=data.get('photo'),
            caption=data.get('ad_text'),
            reply_markup=generate_ad_keyboard(
                text=data.get('button_text'),
                url=data.get('url')
            )
        )
