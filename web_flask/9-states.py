#!/usr/bin/python3
''' starts a Flask web application '''
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__, template_folder='templates/')


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    all_states = storage.all(State)
    if id:
        id = 'State.' + id
    return render_template('9-states.html', states=all_states, s_id=id)


@app.teardown_appcontext
def teardown_db(exception):
    ''' remove the current SQLAlchemy Session '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
