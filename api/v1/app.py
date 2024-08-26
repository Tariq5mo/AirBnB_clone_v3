#!/usr/bin/python3
"""For web application
"""
from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)


@app.teardown_appcontext
def teardown_database(exception=None):
    # Clean up the database session
    storage.close()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

app.register_blueprint(app_views)


if __name__ == "__main__":
    HBNB_API_HOST = getenv("HBNB_API_HOST")
    if not HBNB_API_HOST:
        HBNB_API_HOST = '0.0.0.0'
    HBNB_API_PORT = getenv("HBNB_API_PORT")
    if not HBNB_API_PORT:
        HBNB_API_PORT = 5000
    app.run(host=HBNB_API_HOST, port=int(HBNB_API_PORT), threaded=True, debug=True)
