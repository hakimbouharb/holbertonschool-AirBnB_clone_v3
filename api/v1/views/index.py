#!/usr/bin/python3
"""
start web app
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def get_status():
    """Returns a JSON response with status OK."""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def get_stats():
    """Returns the number of each object type in storage."""
    classes = ["Amenity", "City", "Place", "Review", "State", "User"]
    stats = {}

    for cls_name in classes:
        cls_count = storage.count(cls_name)
        stats[cls_name] = cls_count

    return jsonify(stats)
