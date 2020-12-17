import models

from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required
from playhouse.shortcuts import model_to_dict

trip_bridge = Blueprint('trip_bridges', 'trip_bridge', url_prefix='trip_bridge')

# Create trip relation route
@trip_bridge.route('/', methods=['POST'])
@login_required
def create_trip_relation():
    payload = request.get_json()

    new_trip_bridge = models.Trip_bridge.create(user_ID=current_user.id, trip_ID=payload['trip_ID'])
    trip_bridge = model_to_dict(new_trip_bridge)
    return jsonify(data=trip_bridge, status={'code': 200, 'message': 'Success'})