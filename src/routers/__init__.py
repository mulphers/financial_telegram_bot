from aiogram import Router

from src.routers.admin import admin_router
from src.routers.client import client_router

router = Router(name='main')

router.include_routers(
    client_router,
    admin_router,
)
