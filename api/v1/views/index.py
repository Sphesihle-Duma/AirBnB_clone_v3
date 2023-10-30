#!/usr/bin/python3
"""connecting to API"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", strict_slashes=False, methods=["GET"])
def hbnbStatus():
    """hbnbStatus"""
    return jsonify({"status": "OK"})
