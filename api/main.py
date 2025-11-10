from fastapi import FastAPI
from controller.Pessoa import router as Pessoa_router
from controller.Endereco import router as End_router
from lib.model.models import init_db

app = FastAPI(title="FastAPI + SQLModel - MVC + Repository")


@app.on_event("startup")
def on_startup():
    # cria as tabelas no DB (arquivo sqlite)
    init_db()


app.include_router(Pessoa_router)
app.include_router(End_router)


@app.get("/")
def health():
    return {"status": "ok"}