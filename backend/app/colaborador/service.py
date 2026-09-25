from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.colaborador.schemas import ColaboradorCreate, ColaboradorResponse, ColaboradorUpdate
from app.colaborador.repository import ColaboradorRepository

class ColaboradorService:
    # Helpers functions
    def exist_colaborador_by_id(db: Session, colaborador_id: int):
        colaborador = ColaboradorRepository.get_colaborador_by_id(db=db, colaborador_id=colaborador_id)

        if not colaborador:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Colaborador não encontrado com o ID {colaborador_id}'
            )
        return colaborador

    # Funcions of systems
    def create_colaborador(db: Session, colaborador_data: ColaboradorCreate):
        colaborador_dict = colaborador_data.model_dump()
        return ColaboradorRepository.create_colabordor(db=db, colaborador_data=colaborador_dict)

    def update_colaborador(db: Session, colaborador_id: int, colaborador_update: ColaboradorUpdate):
        colaborador = ColaboradorService.exist_colaborador_by_id(db, colaborador_id)

        colaborador_dict = colaborador_update.model_dump(exclude_unset=True)
        return ColaboradorRepository.update_colaborador(db=db, db_colaborador=colaborador, update_colaborador_data=colaborador_dict)

    def get_all_colaboradores(db: Session, skip: int=0, limit: int=100):
        return ColaboradorRepository.get_all_colaboradores(db=db, skip=skip, limit=limit)

    def get_colaborador_by_id(db: Session, colaborador_id: int):
        colaborador = ColaboradorService.exist_colaborador_by_id(db=db, colaborador_id=colaborador_id)
        return colaborador

    def disable_enable_colaborador(db: Session, colaborador_id: int, status_update: str):
        colaborador = ColaboradorService.exist_colaborador_by_id(db=db, colaborador_id=colaborador_id)

        if not status_update or not status_update.status:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Status não informado!"
            )

        novo_status = status_update.status.value if hasattr(status_update.status, "value") else status_update.status

        return ColaboradorRepository.disable_enable_colaborador(db=db, db_colaborador=colaborador, status_update=novo_status)
