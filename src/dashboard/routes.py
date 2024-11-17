from typing import Annotated

from fastapi import APIRouter, Depends, Request, Response
from fastapi.responses import RedirectResponse

from src.database import User
from src.templates_conf import templates
from src.users.routes import fastapi_users_routers

router = APIRouter(prefix='/dashboard')

CurrentUserDep = Annotated[
    User, Depends(fastapi_users_routers.current_user(optional=True))
]


@router.get('/')
async def dashboard(
    request: Request, response: Response, user: CurrentUserDep
):
    if not user:
        return RedirectResponse('/', status_code=303)

    return templates.TemplateResponse(
        'dashboard.html',
        {'request': request, 'response': response, 'user': user},
    )
