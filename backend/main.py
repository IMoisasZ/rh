import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from dotenv import load_dotenv
from app.colaborador.models import Colaborador
from app.core.database import engine, Base

# Routers
from app.colaborador.router import router as colaborador_router

# Carrega o caminho do servidor
load_dotenv()

# Obtem o caminho que estava no .env
SERVER_PATH = os.getenv("SERVER_PATH")

# Criação da função lifespan para verificar se o caminho do servidor está ok
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        Base.metadata.create_all(bind=engine)
        print("Banco de dados verificado/tabelas criadas com sucesso!")
        yield
    except RuntimeError as e:
        raise RuntimeError(f'Erro ao conectar ao banco de dado. Detalhe: {e}')
# Dados da API e eecução da lifespan 
app = FastAPI(
    title="API RH",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(colaborador_router, prefix="/api/v1")