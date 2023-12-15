from aiogram import F
from aiogram.types import Message

from src.common.dto.user import UserUpdate
from src.common.interfaces.abstract_uow import AbstractUnitOfWork
from src.routers.admin.router import admin_router
from src.utils.decorators import with_database
from src.utils.lexicon import (CANCEL_ADMIN_STATUS_MESSAGE,
                               INFORMATION_FOR_CHANGE_ADMIN_STATUS_COMMAND,
                               SET_ADMIN_STATUS_MESSAGE,
                               USER_NOT_FOUND_MESSAGE)


@admin_router.message(F.text.regexp(r'/set_admin_status (\d+)').group(1).as_('user_id'))
@with_database
async def process_set_admin_status(
        message: Message,
        user_id: int,
        uow: AbstractUnitOfWork
) -> None:
    result = await uow.user.update_user(
        user_id=user_id,
        data=UserUpdate(
            is_admin=True
        )
    )

    if result:
        await message.answer(text=SET_ADMIN_STATUS_MESSAGE)
    else:
        await message.answer(text=USER_NOT_FOUND_MESSAGE)


@admin_router.message(F.text.regexp(r'/cancel_admin_status (\d+)').group(1).as_('user_id'))
@with_database
async def process_cancel_admin_status(
        message: Message,
        user_id: int,
        uow: AbstractUnitOfWork
) -> None:
    result = await uow.user.update_user(
        user_id=user_id,
        data=UserUpdate(
            is_admin=False
        )
    )

    if result:
        await message.answer(text=CANCEL_ADMIN_STATUS_MESSAGE)
    else:
        await message.answer(text=USER_NOT_FOUND_MESSAGE)


@admin_router.message(F.text.regexp(r'(\/set_admin_status|\/cancel_admin_status)( .*)?'))
async def information_for_change_admin_status_command(
        message: Message,
) -> None:
    await message.answer(text=INFORMATION_FOR_CHANGE_ADMIN_STATUS_COMMAND)
