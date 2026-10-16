from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

TAREFAS = []


def criar_tarefa(titulo: str, descricao: str):
    tarefa = {
        "id": len(TAREFAS) + 1,
        "titulo": titulo,
        "descricao": descricao,
        "concluida": False,
        "criado_em": datetime.now().isoformat()
    }

    return tarefa


@app.get("/")
async def index():
    return {"mensagem": ""}


@app.get("/tarefas")
async def listar_tarefas():
    return TAREFAS


@app.post("/tarefas")
async def adicionar_tarefa(titulo: str, descricao: str):
    tarefa_nova = criar_tarefa(titulo, descricao)

    TAREFAS.append(tarefa_nova)

    return {
        "mensagem": "Tarefa criada com sucesso!",
        "tarefa": tarefa_nova
    }