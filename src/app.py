from repo import MemRepo, Task
from flask import Flask, request

app = Flask(__name__)

repo = MemRepo()

@app.route('/')
def index():
    return f'''
        <h1>hello world</h1>

        <p>Entering some basic text</p>

        <button hx-post="/api"
                hx-trigger="click"
                hx-target="#posts"
                hx-swap="outerHTML">
        Add Posts</button> 

        <p>__</p>

        <form hx-post="/api"
              hx-ext="json-enc"
              hx-target="#json"
              hx-swap="outerHTML"
        >
            <label for="name">Task Name</label>
            <input id="name" name="name" type="text">
            <input type="submit" value="Submit">
        </form>

        <div id="posts"></div>
        <div id="json"></div>
        
        <script src="https://unpkg.com/htmx.org@1.8.0" integrity="sha384-cZuAZ+ZbwkNRnrKi05G/fjBX+azI9DNOkNYysZ0I/X5ZFgsmMiBXgDZof30F5ofc" crossorigin="anonymous"></script>
        <script src="https://unpkg.com/htmx.org/dist/ext/json-enc.js"></script>
    '''

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        data =  request.json or {}
        name = data['name'] or ''
        task = Task(name=name)
        repo.add_task(task)
        tasks = repo.get_tasks()
            
        return f'{"".join(str(task.name) for task in tasks)}'
    return 'No data'

