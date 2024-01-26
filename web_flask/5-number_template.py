#!/usr/bin/python3
''' starts a Flask web application '''
from flask import Flask, render_template


app = Flask(__name__, template_folder='../templates/')


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


@app.route('/number/<n>', strict_slashes=False)
def n_type(n):
    try:
        n = int(n)
        return f"{n} is a number"
    except ValueError:
        pass


@app.route('/number_template/<n>', strict_slashes=False)
def n_type_html(n):
    try:
        n = int(n)
        return render_template('5-number.html', number=n)
    except ValueError:
        pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
