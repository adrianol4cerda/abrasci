from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    full_name: str


class UserCreate(schemas.BaseUserCreate):
    full_name: str


class UserUpdate(schemas.BaseUserUpdate):
    full_name: str
