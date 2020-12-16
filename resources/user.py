import models

from flask import request, jsonify, Blueprint
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user
from playhouse.shortcuts import model_to_dict

user = Blueprint('users', 'user', url_prefix='/user')


# Show Route
# @user.route('/', methods=['GET'])
# def get_all_users():
#     try:


# Register Route
@user.route('/register', methods=['POST'])
def register():
    payload = request.get_json()

    payload['email'] = payload['email'].lower()
    try:
        models.Users.get(models.Users.email == payload['email'])
        return jsonify(data={}, status={'code': 401, 'message': 'A user with that name already exists'})
    except models.DoesNotExist:
        payload['password'] = generate_password_hash(payload['password'])
        user = models.Users.create(**payload)

        #starts user session
        login_user(user)

        user_dict = model_to_dict(user)
        print(user_dict)
        print(type(user_dict))

        del user_dict['password']

        return jsonify(data=user_dict, status={'code': 201, 'message': 'Success'})

# Log in Route
@user.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    print('payload:', payload)
    try:
        user = models.Users.get(models.Users.email == payload['email'])
        user_dict = model_to_dict(user)
        if(check_password_hash(user_dict['password'], payload['password'])):
            del user_dict['password']
            login_user(user)
            print(user, 'this is user')
            return jsonify(data=user_dict, status={'code': 200, 'message': 'Success'})
        else:
            return jsonify(data={}, status={'code': 401, 'message': 'Username or Password is incorrect'})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Username or Password is incorrect"})