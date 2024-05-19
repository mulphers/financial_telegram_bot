from typing import Annotated, Any

from aiogram.filters import BaseFilter
from aiogram.types import Message
from fast_depends import Depends, inject

from src.common.markers.gateway import TransactionGatewayMarker
from src.database.core.gateway import DatabaseGateway


class IsAdminFilter(BaseFilter):
    @inject
    async def __call__(
            self,
            message: Message,
            gateway: Annotated[DatabaseGateway, Depends(TransactionGatewayMarker)],
            *args: Any,
            **kwargs: Any
    ) -> bool:
        user_repository = gateway.user_repository()

        return message.from_user.id in map(lambda obj: obj.user_id,
                                           await user_repository.get_list_admin_user()
                                           )
