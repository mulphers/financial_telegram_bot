from datetime import datetime

from sqlalchemy import Column, DateTime


class ModelWithTimeMixin:
    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.now
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        onupdate=datetime.now,
        default=datetime.now
    )
