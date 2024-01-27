#!/usr/bin/python3
''' starts a Flask web application '''
from flask import Flask, render_template
from models import storage

app = Flask(__name__, template_folder='templates/')


@app.route('/states_list', strict_slashes=False)
def states_html():
    all_states = storage.all()
    return render_template('7-states_list.html', states=all_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
