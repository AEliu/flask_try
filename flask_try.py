from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World! <br>This is the index page.'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user(username):
    return 'Hi, %s' % username

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template('hello.html', name=request.form['username'])
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run()
