from flask import request, jsonify
from app import app, mongo
from app.models import User


# get all users from db
@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    return jsonify({'users': [user.json() for user in users]})


# route toget a paritcular user by it's  usr id
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = mongo.db.users.find_one_or_404({'_id': user_id})
    return jsonify(user.json())


# route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = User.from_json(data)
    user_id = mongo.db.users.insert_one(user.json())
    return jsonify({'user_id': str(user_id.inserted_id)})


# route to update a user by it's id
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = User.from_json(data)
    result = mongo.db.users.update_one({'_id': user_id}, {'$set': user.json()})
    if result.modified_count == 1:
        return jsonify({'message': 'User updated successfully'})
    else:
        return jsonify({'error': 'User not found'}), 404

# route to delte a users from db


@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = mongo.db.users.delete_one({'_id': user_id})
    if result.deleted_count == 1:
        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'error': 'User not found'}), 404
