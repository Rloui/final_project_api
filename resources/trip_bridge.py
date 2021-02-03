import models

from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required
from playhouse.shortcuts import model_to_dict
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

trip_bridge = Blueprint('trip_bridges', 'trip_bridge', url_prefix='trip_bridge')

# Create trip relation, this adds current user to a trip
@trip_bridge.route('/', methods=['POST'])
@jwt_required
def create_trip_relation():
    payload = request.get_json()

    new_trip_bridge = models.Trip_bridge.create(user_ID=current_user.id, trip_ID=payload['trip_ID'])
    trip_bridge = model_to_dict(new_trip_bridge)
    return jsonify(data=trip_bridge, status={'code': 200, 'message': 'Success'})