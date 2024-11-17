from pydantic import BaseModel


class PatientAnswers(BaseModel):
    full_name: str
    social_name: str | None = None
    guardian_name: str
    guardian_phone: str
    idade: float
    auto_percepcao: str
    suporte_social: str
    condicoes_cronicas: str | None = None
    medicamentos: int
    internacoes: int
    quedas: str
    visao: str
    audicao: str
    limitacao_fisica: str
    cognicao: str
    humor: str
    atividades_basicas: str
    atividades_instrumentais: str
    incontinencia: str
    perda_peso: str
    abandono: str
    observacoes: str
    points: int


class PatientOut(PatientAnswers):
    id: int
