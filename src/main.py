from typing import Annotated

from fastapi import Depends, FastAPI, Request
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from src.database import get_session
from src.templates_conf import templates

app = FastAPI()

app.mount('/static', StaticFiles(directory='src/static'), name='static')
DatabaseSession = Annotated[Session, Depends(get_session)]


@app.get('/health')
def health():
    return {'ping': 'pong'}


@app.get('/ampi')
def ampi_form_page(request: Request):
    return templates.TemplateResponse('ampi.html', {'request': request})


@app.get('/dbhealth')
def db_health(session: DatabaseSession):
    return {'ping': 'pong'}
