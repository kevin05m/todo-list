from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates', static_folder='static')

todos = []
username = "kevin"
password = "root"

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/app')
def todo():
    return render_template('index.html', todos=todos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    userinp = request.form['uname']
    passinp = request.form['psw']
    if username == userinp and password==passinp:
        return redirect(url_for('todo'))
    else:
        return redirect(url_for('index'))

@app.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    todos.append({'task': todo, 'done': False})
    return redirect(url_for('todo'))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    todo = todos[index]
    if request.method == 'POST':
        todo['task'] = request.form['todo']
        return redirect(url_for('todo'))
    else:
        return render_template('edit.html', todo=todo, index=index)

@app.route('/check/<int:index>')
def check(index):
    todos[index]['done'] = not todos[index]['done']
    return redirect(url_for('todo'))

@app.route('/delete/<int:index>')
def delete(index):
    del todos[index]
    return redirect(url_for('todo'))

@app.errorhandler(404)
def not_found(e):
    return render_template('custom_page.html'), 404

if __name__ == '__main__':
    app.run(debug=True)