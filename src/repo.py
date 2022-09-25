from pydantic import BaseModel

class Task(BaseModel):
    name: str

class MemRepo:
    def __init__(self):
        self.db = []

    def add_task(self, task: Task ):
        self.db.append(task) 

    def get_tasks(self):
        return self.db
