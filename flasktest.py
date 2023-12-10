from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/<name>')
def hello(name):
    return f'hello: {escape(name)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')