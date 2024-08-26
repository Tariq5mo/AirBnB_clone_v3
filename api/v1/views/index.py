#!/usr/bin/python3
"""The index.
"""
import re
from api.v1.views import app_views
from flask import jsonify
from models import storage


classes = {"Amenity": "amenities", "City": "cities", "Place": "places",
           "Review": "reviews", "State": "states", "User": "users"}


@app_views.route("/stats")
def num_objs():
    ''' Retrieves the number of each objects by type '''
    di = {}
    for cls in classes:
        di[classes[cls]] = storage.count(cls)
    return jsonify(di)


@app_views.route("/status")
def foo_status():
    ''' Return the status '''
    return jsonify({'status': 'OK'})
