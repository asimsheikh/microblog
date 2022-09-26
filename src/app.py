from repo import MemRepo, Task
from flask import Flask, request, render_template

app = Flask(__name__)

repo = MemRepo()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        data =  request.json or {}
        if data.get('name'):
            name = data['name'] or ''
            task = Task(name=name)
            repo.add_task(task)
            tasks = repo.get_tasks()
            return f'{"".join(str(task.name) for task in tasks)}'
        if data.get('blog'):
            blog = data['blog']
            title = data['title']
            return f'<p>{title}</p><p>{blog}</p>'

    return 'No data'

