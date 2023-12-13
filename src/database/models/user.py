from sqlalchemy import Boolean, Column, Integer, String

from src.database.models import Base
from src.database.models.base.mixins.with_time import ModelWithTimeMixin


class User(Base, ModelWithTimeMixin):
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=True, default=None)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
