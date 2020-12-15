import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

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

# Show Route
@trip.route('/<id>', methods=['GET'])
def get_one_dog(id):
    print(id, 'reserved word?')
    trip = models.Trip.get_by_id(id)
    print(trip.__dict__)
    return jsonify(data=model_to_dict(trip), status={'code': 200, 'message': 'Success'})

# Create Route
@trip.route('/', methods=['POST'])
def create_trips():
    payload = request.get_json()
    print(type(payload), 'payload')
    trip = models.Trip.create(**payload)
    print(trip.__dict__)
    print(dir(trip))
    print(model_to_dict(trip), 'model to dict')
    trip_dict = model_to_dict(trip)
    return jsonify(data=trip_dict, status={'code': 201, 'message': 'Success'})