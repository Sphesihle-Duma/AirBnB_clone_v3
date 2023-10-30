#!/usr/bin/python3
"""handles all default RESTFul API actions"""

from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from flask import abort, request, jsonify


@app_views.route("/amenities", strict_slashes=False, methods=["GET"])
@app_views.route("/amenities/<amenity_id>", strict_slashes=False,
                 methods=["GET"])
def amenity(amenity_id=None):
    """show amenity and amenity with id"""
    amenity_list = []
    if amenity_id is None:
        all_objs = storage.all(Amenity).values()
        for v in all_objs:
            amenity_list.append(v.to_dict())
        return jsonify(amenity_list)
    else:
        result = storage.get(Amenity, amenity_id)
        if result is None:
            abort(404)
        return jsonify(result.to_dict())
