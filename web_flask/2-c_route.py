#!/usr/bin/python3
"""a script that starts a Flask web application
0.0.0.0, port 5000 """

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """displays Hello HBNB!"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays HBNB"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """display 'C' followed by the value of <text>"""
    text = text.replace('_', ' ')
    return "C {}".format(text)
    #return 'C %s' % text.replace('_', ' ')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
