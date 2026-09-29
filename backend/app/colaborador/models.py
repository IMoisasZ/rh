import enum
from sqlalchemy import Enum as SAEnum
from sqlalchemy import String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone
from typing import Optional, List
from app.core.database import Base

# Definindo o Enum para o campo regime
class RegimeEnum(str, enum.Enum):
    CLT = "CLT"
    PJ = "PJ"
    DIRETORIA = "DIRETORIA"

# Definindo o Enum para campo status
class StatusEnum(str, enum.Enum):
    ATIVO = "ATIVO"
    DESLIGADO = "DESLIGADO"

class Colaborador(Base):
    __tablename__ = "colaborador"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(150), nullable=False)
    status: Mapped[StatusEnum] = mapped_column(SAEnum(StatusEnum), nullable=False, default="ATIVO")
    regime: Mapped[RegimeEnum] = mapped_column(SAEnum(RegimeEnum), nullable=False)
    data_nascimento: Mapped[datetime] = mapped_column(DateTime)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False)
    rg: Mapped[str] = mapped_column(String(9), nullable=False)
    setor_id: Mapped[int] = mapped_column(Integer, nullable=False)
    cargo_id: Mapped[int] = mapped_column(Integer, nullable=False)
    gestor_id: Mapped[int] = mapped_column(Integer, ForeignKey("colaborador.id"), nullable=False)
    data_inicio: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    data_termino: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda:datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=lambda:datetime.now(timezone.utc), onupdate=lambda:datetime.now(timezone.utc))

    """TODO"""
    # Relacionamento do setor_id
    # setor: Mapped["Setor"] = relationship(back_populates="colaboradores")
    
    """TODO"""
    # Relacionamento do cargo_id
    # cargo: Mapped["Cargo"] = relationship(back_populates="colaboradores")

    # Relacionamento do gestor_id
    gestor: Mapped[Optional["Colaborador"]] = relationship(
        "Colaborador",
        remote_side=[id],
        back_populates="subordinados"
    )

    subordinados: Mapped[List["Colaborador"]] = relationship(
        "Colaborador",
        back_populates="gestor"
    )