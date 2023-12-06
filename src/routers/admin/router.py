from aiogram import Router

from src.filters.is_admin import IsAdminFilter

admin_router = Router(name='admin_router')

admin_router.message.filter(IsAdminFilter())
admin_router.callback_query.filter(IsAdminFilter())
