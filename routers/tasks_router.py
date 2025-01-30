from fastapi import APIRouter
from services.task_service import TaskService
from models.task import Task

router = APIRouter()
task_service = TaskService()

@router.post("/tasks")
def create_task(task: Task):
    return task_service.create_task(task)

@router.get("/tasks")
def get_tasks():
    return task_service.get_tasks()