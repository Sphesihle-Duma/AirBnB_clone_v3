#!/usr/bin/python3
"""connecting to API"""
import os
from models import storage
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify, make_response
from flask_cors import CORS


def create_app():
    """ Creating the flask app """
    app = Flask(__name__)
    app.register_blueprint(app_views)
    cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})

    @app.errorhandler(404)
    def page_not_found(error):
        """Handle 404 Not Found errors"""
        return make_response(jsonify({'error': 'Not found'}), 404)
    return app


def teardown_appcontext(error):
    """Function to be called when the application context is torn down"""
    storage.close()


if __name__ == "__main__":
    app = create_app()
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', '5000')),
            threaded=True)
