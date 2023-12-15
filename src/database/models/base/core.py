import re

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    __abstract__: bool = True

    @classmethod  # type: ignore
    @declared_attr  # type: ignore
    def __tablename__(cls) -> str:
        return re.sub(
            pattern=r'[A-Z]',
            repl=lambda match_obj: f'_{match_obj.group(0).lower()}',
            string=cls.__name__
        )[1:]
