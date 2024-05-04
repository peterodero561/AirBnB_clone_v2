
#!/usr/bin/python3
'''starts a Flask web application tha listens on 0.0.0.0 port 5000'''
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    '''Removes current SQLAchemy Session'''
    storage.close()


@app.route('/states_list', strict_slashes=False)
def statesList():
    '''displays html with lists of all state objects'''
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
