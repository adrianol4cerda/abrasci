from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from src.dashboard.routes import router as dashboard_router
from src.database import Patient, User, get_async_session
from src.patient.schemas import PatientAnswers
from src.templates_conf import templates
from src.users.routes import auth_backend, fastapi_users_routers
from src.users.schemas import UserCreate, UserRead, UserUpdate

app = FastAPI()
app.include_router(
    fastapi_users_routers.get_auth_router(auth_backend), tags=['auth']
)
app.include_router(
    fastapi_users_routers.get_register_router(UserRead, UserCreate),
    tags=['register'],
)
app.include_router(
    fastapi_users_routers.get_users_router(UserRead, UserUpdate),
    prefix='/users',
    tags=['users'],
)
app.include_router(dashboard_router, tags=['Dashboard'])

app.mount('/static', StaticFiles(directory='src/static'), name='static')

DatabaseSessionDep = Annotated[Session, Depends(get_async_session)]
CurrentUserDep = Annotated[User, Depends(fastapi_users_routers.current_user())]
OptionalUserDep = Annotated[
    User, Depends(fastapi_users_routers.current_user(optional=True))
]
CurrentSuperUserDep = Annotated[
    User, Depends(fastapi_users_routers.current_user(superuser=True))
]


@app.get('/health')
def health():
    return {'ping': 'pong'}


@app.get('/dbhealth')
def db_health(session: DatabaseSessionDep):
    return {'ping': 'pong'}


@app.get('/ampi')
def ampi_form_page(request: Request):
    return templates.TemplateResponse('ampi.html', {'request': request})


@app.get('/')
async def login_page(request: Request, user: OptionalUserDep):
    if user:
        return RedirectResponse(url='/dashboard')
    return templates.TemplateResponse('login.html', {'request': request})


@app.get('/register')
async def register_page(request: Request, user: CurrentSuperUserDep):
    return templates.TemplateResponse('register.html', {'request': request})


@app.get('/usuarios')
async def get_users_page(
    request: Request,
    user: CurrentSuperUserDep,
    session: Annotated[AsyncSession, Depends(get_async_session)],
):
    users = await session.scalars(select(User))
    return templates.TemplateResponse(
        'users.html', {'request': request, 'users': users}
    )


@app.get('/usuarios/deletar/{user_id}')
async def delete_user(
    user_id: int,
    session: Annotated[AsyncSession, Depends(get_async_session)],
    user: CurrentUserDep,
):
    user_to_delete = await session.scalar(
        select(User).where(User.id == user_id)
    )

    await session.delete(user_to_delete)
    await session.commit()

    return RedirectResponse(
        url='/usuarios'
    )  # Redirect back to patient list page


@app.post('/save-answers')
async def save_ampi_answers(
    user: CurrentUserDep,
    session: Annotated[AsyncSession, Depends(get_async_session)],
    answers: PatientAnswers,
):
    new_patient = Patient(**answers.model_dump())

    session.add(new_patient)
    await session.commit()

    return {'message': 'success'}


@app.get('/pacientes')
async def get_patients(
    request: Request,
    user: CurrentUserDep,
    session: Annotated[AsyncSession, Depends(get_async_session)],
):
    patients = await session.scalars(select(Patient))

    return templates.TemplateResponse(
        'patients.html', {'request': request, 'patients': patients}
    )


@app.get('/pacientes/deletar/{patient_id}')
async def delete_patient(
    patient_id: int,
    session: Annotated[AsyncSession, Depends(get_async_session)],
    user: CurrentUserDep,
):
    patient = await session.scalar(
        select(Patient).where(Patient.id == patient_id)
    )

    await session.delete(patient)
    await session.commit()

    return RedirectResponse(
        url='/pacientes'
    )  # Redirect back to patient list page


@app.get('/pacientes/editar/{patient_id}')
async def edit_patient_page(
    request: Request,
    patient_id: int,
    user: CurrentUserDep,
    session: Annotated[AsyncSession, Depends(get_async_session)],
):
    patient = await session.scalar(
        select(Patient).where(Patient.id == patient_id)
    )

    if patient is None:
        raise HTTPException(status_code=404, detail='Paciente não encontrado')

    return templates.TemplateResponse(
        'edit_patient.html', {'request': request, 'patient': patient}
    )


@app.post('/pacientes/editar/{patient_id}')
async def update_patient(
    patient_id: int,
    request: Request,
    session: Annotated[AsyncSession, Depends(get_async_session)],
    user: CurrentUserDep,
    answers: PatientAnswers,
):
    patient = await session.scalar(
        select(Patient).where(Patient.id == patient_id)
    )

    if patient is None:
        raise HTTPException(status_code=404, detail='Paciente não encontrado')

    for key, value in answers.model_dump(exclude_unset=True).items():
        setattr(patient, key, value)

    await session.commit()

    return {'message': 'ok'}
