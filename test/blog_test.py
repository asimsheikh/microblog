import requests
from src.repo import MemRepo, Blog

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
    assert 'Blog' in requests.get('http://127.0.0.1:5000/').text
