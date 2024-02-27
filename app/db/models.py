from datetime import datetime
# from pydantic import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.types import DateTime, Integer, String, Text
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    # relationship
)


class Base(DeclarativeBase):
    pass


class User(Base):
    __table_name__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] | None = mapped_column(String(50))
    tg_id: Mapped[int] = mapped_column(Integer)


class Question(Base):
    __table_name__ = 'questions'

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(Text)
    sequence_number: Mapped[int] = mapped_column(Integer)
    theme: Mapped[int] = mapped_column(ForeignKey("Theme.id"))
    answer: Mapped[int] = mapped_column(String(256))
    commentary: Mapped[str] | None = mapped_column(Text)


class Theme(Base):
    __table_name__ = 'themes'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(Text)
    package: Mapped[int] = mapped_column(ForeignKey("Package.id"))


class Package(Base):
    __table_name__ = 'packages'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(Text)
    game: Mapped[int] = mapped_column(ForeignKey("Game.id"))


class Game(Base):
    __table_name__ = 'games'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(Text)


class Result(Base):
    __table_name__ = 'results'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    question_id: Mapped[int] = mapped_column(Integer)
    time: Mapped[datetime] = mapped_column(DateTime)
