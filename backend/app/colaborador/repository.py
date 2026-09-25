from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.colaborador.models import Colaborador

class ColaboradorRepository:
    @staticmethod
    def create_colabordor(db: Session, colaborador_data: dict) -> Colaborador:
        try:
            db_colaborador = Colaborador(**colaborador_data)
            db.add(db_colaborador)
            db.commit()
            db.refresh(db_colaborador)
            return db_colaborador
        except SQLAlchemyError as e:
            db.rollback()
            raise e

    @staticmethod
    def update_colaborador(db: Session, db_colaborador: Colaborador, update_colaborador_data: dict) -> Colaborador:
        try:
            for key, value in update_colaborador_data.items():
                setattr(db_colaborador, key, value)

            db.commit()
            db.refresh(db_colaborador)
            return db_colaborador
        except SQLAlchemyError as e:
            db.rollback()
            raise e

    @staticmethod
    def get_all_colaboradores(db: Session, skip: int=0, limit: int=100) -> list[Colaborador]:
        try:
            return db.query(Colaborador).offset(skip).limit(limit).all()
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def get_colaborador_by_id(db: Session, colaborador_id: int) -> Colaborador | None:
        try:
            return db.query(Colaborador).filter(Colaborador.id == colaborador_id).first()
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def disable_enable_colaborador(db: Session, db_colaborador: Colaborador, status_update: str) -> Colaborador:
        try:
            db_colaborador.status = status_update

            db.commit()
            db.refresh(db_colaborador)
            return db_colaborador
        except SQLAlchemyError as e:
            db.rollback()
            raise e