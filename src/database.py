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
#AMPI-AB
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
#SNELLEN (VISÃO)
    snellen: Mapped[str] = mapped_column(nullabe=True)
#SUSSURRO (AUDIÇÃO)
    sussurro: Mapped[str] = mapped_column(nullable=True)
#KATZ (INDEPENDENCIA)
    banho: Mapped[str] = mapped_column(nullable=True)
    vestir: Mapped[str] = mapped_column(nullable=True)
    banheiro: Mapped[str] = mapped_column(nullable=True)
    transferencia: Mapped[str] = mapped_column(nullable=True)
    continencia: Mapped[str] = mapped_column(nullable=True)
    alimentacao: Mapped[str] = mapped_column(nullable=True)
#LAWTON (INDEPENDENCIA)
    telefone: Mapped[str] = mapped_column(nullable=True)
    mobilidade: Mapped[str] = mapped_column(nullable=True)
    compras: Mapped[str] = mapped_column(nullable=True)
    cozinhar: Mapped[str] = mapped_column(nullable=True)
    limpar: Mapped[str] = mapped_column(nullable=True)
    reparos: Mapped[str] = mapped_column(nullable=True)
    lavar_roupas: Mapped[str] = mapped_column(nullable=True)
    tomar_remedio: Mapped[str] = mapped_column(nullable=True)
    financas: Mapped[str] = mapped_column(nullable=True)
#MARCHA (VELOCIDADE)
    primeira_med: Mapped[float] = mapped_column(nullable=True)
    segunda_med: Mapped[float] = mapped_column(nullable=True)
    terceira_med: Mapped[float] = mapped_column(nullable=True)
    vel_marcha: Mapped[float] = mapped_column(nullable=True)
#DEPRESSÃO GERIÁTRICA
    satisfacao: Mapped[str] = mapped_column(nullable=True)
    atividade: Mapped[str] = mapped_column(nullable=True)
    felicidade: Mapped[str] = mapped_column(nullable=True)
    casa: Mapped[str] = mapped_column(nullable=True)
    pontuacao: Mapped[int] = mapped_column(nullable=True)
#COGNIÇÃO
    dia_do_mes: Mapped[str] = mapped_column(nullable=True)
    mes: Mapped[str] = mapped_column(nullable=True)
    ano: Mapped[str] = mapped_column(nullable=True)
    memoria: Mapped[str] = mapped_column(nullable=True)
    fluencia: Mapped[str] = mapped_column(nullable=True)
    ajuste_escolaridade: Mapped[str] = mapped_column(nullable=True)
    soma_cognicao: Mapped[int] = mapped_column(nullable=True)




