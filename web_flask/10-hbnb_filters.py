''' starts a Flask web application '''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__, template_folder='templates/')


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    all_states = storage.all(State)
    all_amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                           states=all_states, amenities=all_amenities)


@app.teardown_appcontext
def teardown_db(exception):
    ''' remove the current SQLAlchemy Session '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
