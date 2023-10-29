#!/usr/bin/python3
"""connecting to API"""
from api.v1.views import app_views
from flask import jsonify

def hbnbStatus():
    """hbnbStatus"""
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    app_views.run(host='0.0.0.0', port=5000)
