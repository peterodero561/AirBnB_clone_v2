#!/usr/bin/python3
'''Script that starts a web application'''
from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    if n % 2 == 0:
        return render_template(
                '6-number_odd_or_even.html', n=str(n) + ' is even')
    else:
        return render_template(
                '6-number_odd_or_even.html', n=str(n) + ' is odd')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
