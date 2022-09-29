from repo import MemRepo, Blog
from flask import Flask, request, render_template

app = Flask(__name__)

repo = MemRepo()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alpinejs')
def alpine():
    return render_template('alpine.html')

@app.route('/microblog')
def microblog():
    return render_template('microblog.html')

@app.route('/editor')
def editor():
    return render_template('editor.html')

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        data =  request.json or {}
        blog = Blog(title=data['title'], blog=data['blog'])
        repo.add_blog(blog)
        blogs= repo.get_blogs()
            
        return f'{"<br>".join(str(blog) for blog in blogs)}'
    return 'No data'

