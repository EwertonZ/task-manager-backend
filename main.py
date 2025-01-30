from fastapi import FastAPI
from routers import tasks_router

app = FastAPI()

# Inclui o router para as rotas de tarefas
app.include_router(tasks_router.router, prefix="/api/v1")