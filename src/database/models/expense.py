from sqlalchemy import Column, Float, ForeignKey, Integer, String

from src.database.models import Base
from src.database.models.base.mixins.with_time import ModelWithTimeMixin


class Expense(Base, ModelWithTimeMixin):
    expense_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(ForeignKey('user.user_id', ondelete='CASCADE'))
    amount_expense = Column(Float)
    short_description = Column(String(length=32))
