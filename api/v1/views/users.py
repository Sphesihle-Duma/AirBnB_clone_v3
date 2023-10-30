#!/usr/bin/python3
"""User objects that handles all default RESTFul API actions"""

from api.v1.views import app_views
from models import storage
from models.user import User
from flask import abort, request, jsonify


@app_views.route("/users", strict_slashes=False, methods=["GET"])
@app_views.route("/users/<user_id>", strict_slashes=False,
                 methods=["GET"])
def user(user_id=None):
    """show user in dbstorage"""
    user_list = []
    if user_id is None:
        all_objs = storage.all(User).values()
        for v in all_objs:
            user_list.append(v.to_dict())
        return jsonify(user_list)
    else:
        result = storage.get(User, user_id)
        if result is None:
            abort(404)
        return jsonify(result.to_dict())
