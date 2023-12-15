from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models import Base
from src.database.models.base.mixins.with_time import ModelWithTimeMixin


class Expense(Base, ModelWithTimeMixin):
    expense_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.user_id', ondelete='CASCADE'))
    amount_expense: Mapped[float] = mapped_column(Float)
    short_description: Mapped[str] = mapped_column(String(length=32))
