#!/usr/bin/python3
"""a script that starts a Flask web application
0.0.0.0, port 5000 """

from flask import Flask, render_template
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

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text = "is_cool"):
    """display 'Python followed by the value of <text>"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """displays '<n> is a number' only if 'n' is an integer"""
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """displays a HTML page that contains 'Number: n' only
    if 'n' is an integer"""
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")