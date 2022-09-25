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

def test_initial():
    assert True 

def test_can_add_todo():
    repo = MemRepo()
    repo.add_task(1)
    assert repo.get_tasks() == [1]

    repo.add_task(2)
    assert repo.get_tasks() == [1,2]

