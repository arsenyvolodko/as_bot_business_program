from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import DateTime
from datetime import datetime

from as_bot_business_program.enums.answer_status_enum import AnswerStatusEnum
from as_bot_business_program.enums.service_name_enum import ServiceNameEnum


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=False,
    )

    username: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
    )


class Request(Base):
    __tablename__ = "request"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    user_id = Column(
        BigInteger,
        ForeignKey("user.id"),
        nullable=False,
    )

    text: Mapped[str] = mapped_column(nullable=False)

    service: Mapped[ServiceNameEnum] = mapped_column(
        nullable=False,
    )

    status: Mapped[AnswerStatusEnum] = mapped_column(
        nullable=False, default=AnswerStatusEnum.IGNORED
    )

    time = Column(DateTime, nullable=False, default=datetime.now)

    source_chat_msg_text: Mapped[str] = mapped_column(nullable=True)
    common_chat_msg_text: Mapped[str] = mapped_column(nullable=True)

    source_chat_msg_id = Column(
        BigInteger,
        nullable=True,
    )

    common_chat_msg_id = Column(
        BigInteger,
        nullable=True,
    )
