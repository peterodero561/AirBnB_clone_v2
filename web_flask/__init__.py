#!/usr/bin/python3
'''Init file'''
from flask import Flask


def create_app():
    '''creating flask app'''
    app = Flask(__name__)

    # Register blueprints
    from my_flask_app.routes.main import main_bp
    app.register_blueprint(main_bp)

    return app
