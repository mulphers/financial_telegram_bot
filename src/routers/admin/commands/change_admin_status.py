from aiogram import F
from aiogram.types import Message

from src.common.dto.user import UserUpdate
from src.common.interfaces.abstract_uow import AbstractUnitOfWork
from src.routers.admin.router import admin_router
from src.utils.decorators import with_database


@admin_router.message(F.text.regexp(r'/set_admin_status (\d+)').group(1).as_('user_id'))
@with_database
async def process_set_admin_status(
        message: Message,
        user_id: int,
        uow: AbstractUnitOfWork
):
    result = await uow.user.update_user(
        user_id=user_id,
        data=UserUpdate(
            is_admin=True
        )
    )

    if result:
        await message.answer(text=f'User {user_id} has been assigned the position of administrator.')
    else:
        await message.answer(text=f'User {user_id} does not exist')


@admin_router.message(F.text.regexp(r'/cancel_admin_status (\d+)').group(1).as_('user_id'))
@with_database
async def process_cancel_admin_status(
        message: Message,
        user_id: int,
        uow: AbstractUnitOfWork
):
    result = await uow.user.update_user(
        user_id=user_id,
        data=UserUpdate(
            is_admin=False
        )
    )

    if result:
        await message.answer(text=f'User {user_id} has been removed as administrator')
    else:
        await message.answer(text=f'User {user_id} does not exist')
