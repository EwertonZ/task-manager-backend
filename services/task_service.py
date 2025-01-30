from pymongo import MongoClient
from models.task import Task
from core.config import settings
from fastapi.encoders import jsonable_encoder

class TaskService:
    def __init__(self):
        self.client = MongoClient(settings.mongo_uri)
        self.db = self.client.task_manager
        self.collection = self.db.tasks

    def create_task(self, task: Task):
        task_dict = task.model_dump()  
        result = self.collection.insert_one(task_dict)
        task_dict["_id"] = str(result.inserted_id)        
        return task_dict 

    def get_tasks(self):
        tasks = list(self.collection.find())  # Obtém todas as tarefas
        # Mapeia cada tarefa e converte o _id para str
        for task in tasks:
            task["_id"] = str(task["_id"])
        return tasks  # Retorna as tarefas com _id convertido para str