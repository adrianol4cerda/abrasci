from typing import Annotated, Final

from fastapi import Depends, Request
from fastapi_users import (
    BaseUserManager,
    FastAPIUsers,
    IntegerIDMixin,
)
from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy,
)
from fastapi_users.db import BaseUserDatabase

from src.database import User, get_user_db
from src.settings import Settings

cookie_transport = CookieTransport(cookie_max_age=3600)

SECRET: Final = Settings().SECRET_KEY


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name='cookie',
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET

    async def on_after_register(
        self, user: User, request: Request | None = None
    ) -> None:
        print(f'User {user.id} has registered')


async def get_user_manager(
    user_db: Annotated[BaseUserDatabase, Depends(get_user_db)],
):
    yield UserManager(user_db)


fastapi_users_routers = FastAPIUsers[User, int](
    get_user_manager, [auth_backend]
)
