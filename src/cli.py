import asyncio
import contextlib

from fastapi_users.exceptions import UserAlreadyExists
from typer import Typer

from src.database import get_async_session, get_user_db
from src.users.routes import get_user_manager
from src.users.schemas import UserCreate

app = Typer()

get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


async def create_admin_user(
    email: str, password: str, is_superuser: bool = False
):
    try:
        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    user = await user_manager.create(
                        UserCreate(
                            full_name='Admin',
                            email=email,
                            password=password,
                            is_superuser=is_superuser,
                        )
                    )
                    print(f'User created {user}')
                    return user
    except UserAlreadyExists:
        print(f'User {email} already exists')
        raise


@app.command()
def create(email: str, password: str, is_superuser: bool):
    asyncio.run(create_admin_user(email, password, is_superuser))
