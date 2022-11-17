#!/usr/bin/python3
""" a script that starts a flask web application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def states():
    """Displays a HTML page with a list of all state objects in DBStorage"""
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """ Removes the current SQLALchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
