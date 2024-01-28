''' starts a Flask web application '''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__, template_folder='templates/')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    all_states = storage.all(State)
    all_amenities = storage.all(Amenity)
    all_places = storage.all(Place)
    return render_template('100-hbnb.html',
                           states=all_states, amenities=all_amenities,
                           places=all_places)


@app.teardown_appcontext
def teardown_db(exception):
    ''' remove the current SQLAlchemy Session '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
