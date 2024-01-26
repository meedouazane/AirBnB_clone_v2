#!/usr/bin/python3
''' starts a Flask web application '''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text_c(text):
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python', strict_slashes=False)
def text_python_default():
    return "Python is cool"


@app.route('/python/<text>', strict_slashes=False)
def text_python(text):
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def n_type(n):
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)