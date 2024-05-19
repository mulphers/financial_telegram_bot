from typing import Annotated

from aiogram import Bot
from fast_depends import Depends, inject

from src.common.keyboards.keyboard_generator import generate_ad_keyboard
from src.common.markers.gateway import TransactionGatewayMarker
from src.database.core.gateway import DatabaseGateway


@inject
async def send_ad_all_active_users(
        bot: Bot,
        data: dict[str, str],
        gateway: Annotated[DatabaseGateway, Depends(TransactionGatewayMarker)]
) -> None:
    user_repository = gateway.user_repository()

    for user in await user_repository.get_list_active_user():
        await bot.send_photo(
            chat_id=user.user_id,
            photo=data['photo'],
            caption=data['ad_text'],
            reply_markup=generate_ad_keyboard(
                text=data['button_text'],
                url=data['url']
            )
        )
