from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional
from app.colaborador.models import StatusEnum, RegimeEnum
from app.core.text_validator import clean_and_validate_string

MIN_LENGTH_NOME = 15
MIN_LENGTH_CPF = 11
MIN_LENGTH_RG = 9

class ColaboradorCreate(BaseModel):
    """
        min_length_nome = minimo de caracteres para o nome
        min_length_cpf = minimo de caracteres para o cpf
        min_length_rg = minimo de caracteres para o rg
    """
    nome: str = Field(..., min_length=MIN_LENGTH_NOME, description=f'O nome do colaborador deve ter no minimo {MIN_LENGTH_NOME} caracteres')
    status: StatusEnum = StatusEnum.ATIVO
    regime: RegimeEnum
    data_nascimento: Optional[datetime] = None
    cpf: str = Field(..., min_length=MIN_LENGTH_CPF, description=f"O CPF deve ter exatos {MIN_LENGTH_CPF} digitos!")
    rg: str = Field(..., min_length=MIN_LENGTH_RG, description=f"O RG deve ter no minimo {MIN_LENGTH_RG} digitos!")
    setor_id: int
    cargo_id: int
    gestor_id: Optional[int] = None
    data_inicio: datetime
    data_termino: Optional[datetime] = None

    @field_validator("nome")
    @classmethod
    def validate_nome(cls, v: str):
        cleaned = clean_and_validate_string(v, MIN_LENGTH_NOME)
        return cleaned.upper()

class ColaboradorUpdate(BaseModel):
    nome: Optional[str] = None
    regime: Optional[RegimeEnum] = None
    data_nascimento: Optional[datetime] = None
    cpf: Optional[str] = None
    rg: Optional[str] = None
    setor_id: Optional[int] = None
    cargo_id: Optional[int] = None
    gestor_id: Optional[int] = None
    data_inicio: Optional[datetime] = None

    @field_validator("nome")
    @classmethod
    def update_nome(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return None

        cleaned = clean_and_validate_string(v, MIN_LENGTH_NOME)
        return cleaned.upper()

class ColaboradorResponse(BaseModel):
    id: int
    nome: str
    status: StatusEnum
    regime: RegimeEnum
    data_nascimento: datetime
    cpf: str
    rg: str
    setor_id: int
    cargo_id: int
    gestor_id: Optional[int]
    data_inicio: datetime
    data_termino: Optional[datetime]
    created_at: datetime

    model_config = {'from_attributes': True}

class ColaboradorStatusUpdate(BaseModel):
    status: StatusEnum = Field(..., description="Status do colaborador: ATIVO ou DESLIGADO")

