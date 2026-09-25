from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.core.database import get_db
from app.colaborador.schemas import ColaboradorCreate, ColaboradorResponse, ColaboradorUpdate, ColaboradorStatusUpdate
from app.colaborador.service import ColaboradorService

router = APIRouter(prefix="/colaboradores", tags=["Colaboradores"])

@router.post("/", response_model=ColaboradorResponse, status_code=status.HTTP_201_CREATED)
def create_colaborador(colaborador_data: ColaboradorCreate, db: Session = Depends(get_db)):
    try:
        return ColaboradorService.create_colaborador(db=db, colaborador_data=colaborador_data)
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Não foi possivel incluir o colaborador {colaborador_data.nome}!'
        )

@router.put("/{colaborador_id}", response_model=ColaboradorResponse, status_code=status.HTTP_200_OK)
def update_colaborador(colaborador_id: int, colaborador_update: ColaboradorUpdate, db: Session = Depends(get_db)):
    try:
        return ColaboradorService.update_colaborador(db=db, colaborador_id=colaborador_id, colaborador_update=colaborador_update)
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Não foi possivel alterar o colaborador com ID {colaborador_id}'
        )

@router.get("/", response_model=list[ColaboradorResponse], status_code=status.HTTP_200_OK)
def get_all_colaboradores(db: Session = Depends(get_db), skip: int=0, limit: int=100):
    try:
        return ColaboradorService.get_all_colaboradores(db=db, skip=skip, limit=limit)
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro interno. Tente novamente mais tarde!"
        )

@router.get("/{colaborador_id}", response_model=ColaboradorResponse, status_code=status.HTTP_200_OK)
def get_colaborador_by_id(colaborador_id: int, db:Session = Depends(get_db)):
    try:
        return ColaboradorService.get_colaborador_by_id(db=db, colaborador_id=colaborador_id)
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro interno. Tente novamente mais tarde!"
        )

@router.patch("/{colaborador_id}", response_model=ColaboradorResponse, status_code=status.HTTP_200_OK)
def disable_enable_colaborador(colaborador_id: int, status_update: ColaboradorStatusUpdate, db: Session = Depends(get_db)):
    try:
        return ColaboradorService.disable_enable_colaborador(db=db, colaborador_id=colaborador_id, status_update=status_update)
    except SQLAlchemyError as e:
        print(f"ERRO REAL DO BANCO: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Não foi possivel relizar a alteração do colaborador de ID {colaborador_id}!'
        )