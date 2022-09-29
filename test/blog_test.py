import requests
from src.repo import MemRepo, Blog

def test_initial():
    assert True 

def test_can_add_todo():
    repo = MemRepo()
    blog = Blog(title='First blog', blog='Entering some information')
    repo.add_blog(blog)
    assert repo.get_blogs() == [blog]

    repo.add_blog(blog)
    assert repo.get_blogs() == [blog, blog]

def test_flask_app_running():
    assert 'enter color name' in requests.get('http://127.0.0.1:5000/').text
