from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager

import models

from resources.trips import trip
from resources.user import user
from resources.trip_bridge import trip_bridge

login_manager = LoginManager()

DEBUG = True
PORT = 8000

app = Flask(__name__)

app.secret_key = 'FJSGPOFVNAPIGFHVFSHF'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    try:
        return models.Users.get(models.Users.id == userid)
    except models.DoesNotExist:
        return None

@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response

CORS(trip, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(trip, url_prefix='/api/v1/trips')

CORS(user, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(user, url_prefix='/user')

CORS(trip_bridge, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(trip_bridge, url_prefix='/trip_bridge')

@app.route('/')
def index():
    return 'hi'

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)