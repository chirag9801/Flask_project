from flask import Flask, render_template, request, redirect

# special python variable __name__ indicates root path of app
app = Flask(__name__)

# to store tasks
tasks = []


# / maps the url to index function
@app.route('/')


def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])

def add():
    task = request.form.get('task')
    tasks.append(task)
    return redirect('/')

@app.route('/delete/<int:index>')

def delete(index):
    if index< len(tasks):
        del tasks[index]
    return redirect('/')

if __name__ == '__main__':
    app.run()
