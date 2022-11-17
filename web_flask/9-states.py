#!/usr/bin/python3
""" a script that starts a flask web application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Displays a HTML page with a list of all state objects in DBStorage"""
    states = storage.all('State')
    return render_template('9-states.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays a HTML page with a list of info about <id> if it exists"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(self):
    """ Removes the current SQLALchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
