import requests
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
    task = Task(name="Go shopping")
    repo.add_task(task)
    assert repo.get_tasks() == [task]

    repo.add_task(task)
    assert repo.get_tasks() == [task,task]

def test_flask_app_running():
    assert 'hello' in requests.get('http://127.0.0.1:5000/').text
