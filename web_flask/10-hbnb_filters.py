#!/usr/bin/python3
""" a script that starts a flask web application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays a HTML page with a list of all state objects in DBStorage"""
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters.html',
                            states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(self):
    """ Removes the current SQLALchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
