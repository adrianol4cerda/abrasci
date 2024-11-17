from enum import Enum
from typing import Annotated, AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import (
    create_async_engine,
)
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.settings import Settings

engine = create_async_engine(Settings().DATABASE_URL)


class Base(DeclarativeBase):
    pass


class UserRole(str, Enum):
    ADMIN = 'admin'
    USER = 'user'


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(primary_key=True)  # type: ignore
    full_name: Mapped[str]


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(engine) as session:
        yield session


async def get_user_db(
    session: Annotated[AsyncSession, Depends(get_async_session)],
):
    yield SQLAlchemyUserDatabase(session, User)


class Patient(Base):
    __tablename__ = 'patient'

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str]
    social_name: Mapped[str] = mapped_column(nullable=True)
    guardian_name: Mapped[str]
    guardian_phone: Mapped[str]
    idade: Mapped[float]
    auto_percepcao: Mapped[str]
    suporte_social: Mapped[str]
    condicoes_cronicas: Mapped[str]
    medicamentos: Mapped[int]
    internacoes: Mapped[int]
    quedas: Mapped[str]
    visao: Mapped[str]
    audicao: Mapped[str]
    limitacao_fisica: Mapped[str]
    cognicao: Mapped[str]
    humor: Mapped[str]
    atividades_basicas: Mapped[str]
    atividades_instrumentais: Mapped[str]
    incontinencia: Mapped[str]
    perda_peso: Mapped[str]
    abandono: Mapped[str]
    observacoes: Mapped[str] = mapped_column(nullable=True)
    points: Mapped[int]
