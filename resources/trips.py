import models

from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required
from playhouse.shortcuts import model_to_dict
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

trip = Blueprint('trips', 'trip')

# Index Route
@trip.route('/', methods=['GET'])
def get_all_trips():
    try:
        trips = [model_to_dict(trip) for trip in models.Trip.select()]
        print(trips)
        return jsonify(data=trips, status={'code': 200, 'message': 'Success'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 401, 'message': 'Error getting the resources'})

# Current User Trip Index Route
@trip.route('/users', methods=['GET'])
@jwt_required
def get_all_user_trips(current_user):
    try:
        trips = [model_to_dict(trip_bridge) for trip_bridge in models.Trip_bridge.select().where(models.Trip_bridge.user_ID == current_user.id)]
        print(trips)
        return jsonify(data=trips, status={'code': 200, 'message': 'Success'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 401, 'message': 'Error getting the resources'})

# Show Route
@trip.route('/<id>', methods=['GET'])
def get_one_trip(id):
    print(id, 'reserved word?')
    trip = models.Trip.get_by_id(id)
    print(trip.__dict__)
    return jsonify(data=model_to_dict(trip), status={'code': 200, 'message': 'Success'})

# Create Route
@trip.route('/', methods=['POST'])
@jwt_required
def create_trips():
    payload = request.get_json()
    print(type(payload), 'payload')
    trip = models.Trip.create(**payload)
    print(trip.__dict__)
    print(dir(trip))
    print(model_to_dict(trip), 'model to dict')
    trip_dict = model_to_dict(trip)
    new_trip_bridge = models.Trip_bridge.create(user_ID=current_user.id, trip_ID=trip_dict['id'])
    return jsonify(data=trip_dict, status={'code': 201, 'message': 'Trip Creation Success'})

# Update Route
@trip.route('/<id>', methods=['PUT'])
def  updated_trip(id):
    payload = request.get_json()
    query = models.Trip.update(**payload).where(models.Trip.id==id)
    query.execute()
    return jsonify(data=model_to_dict(models.Trip.get_by_id(id)), status={'code': 200, 'message': 'resource updated successfully'})

# Delete Route
@trip.route('/<id>', methods=['Delete'])
def delete_trip(id):
    query = models.Trip.delete().where(models.Trip.id==id)
    query.execute()
    return jsonify(data='resource successfully deleted', status={'code': 200, 'message': 'resource deleted successfully'})