from flask import Blueprint, request, jsonify
from services.user_service import *

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/')
def health():
    return jsonify({'status': 'OK'}), 200

@user_routes.route('/users', methods=['GET'])
def get_all():
    return jsonify(get_all_users()), 200

@user_routes.route('/users', methods=['POST'])
def create():
    data = request.get_json()
    user = create_user(data)
    if user: return jsonify(user), 201
    return jsonify({'error': 'Invalid input'}), 400

@user_routes.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user: return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

@user_routes.route('/user/<int:user_id>', methods=['PUT'])
def update(user_id):
    data = request.get_json()
    user = update_user(user_id, data)
    if user: return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

@user_routes.route('/user/<int:user_id>', methods=['DELETE'])
def delete(user_id):
    if delete_user(user_id): return jsonify({'message': 'User deleted'}), 200
    return jsonify({'error': 'User not found'}), 404

@user_routes.route('/search')
def search():
    name = request.args.get('name')
    return jsonify(search_user_by_name(name)), 200

@user_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if login_user(data): return jsonify({'message': 'Login success'}), 200
    return jsonify({'error': 'Invalid credentials'}), 401
  
