from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World! <br>This is the index page.'

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/user/<username>')
def show_user(username):
    return 'Hi, %s' % username

if __name__ == '__main__':
    app.run()
