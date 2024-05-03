#!/usr/bin/python3
'''Script that starts a web application'''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    '''return Hello HBNB'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''return HBNB'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    '''return c and some text'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    '''returns python and some text'''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    if n.isdigit():
        return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
