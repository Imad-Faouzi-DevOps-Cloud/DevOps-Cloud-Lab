# app/routes.py

from flask import Blueprint, jsonify, request

# Create a blueprint called 'user' to group all user-related routes
user_bp = Blueprint('user', __name__)

# This will act as our simple in-memory "database" of users
# In a real app, this would be a proper database like PostgreSQL
users = []

# Route to get all users
# HTTP GET on /users returns the list of all users as JSON
@user_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200  # Return users list with HTTP status 200 (OK)

# Route to create a new user
# HTTP POST on /users with JSON body containing 'name' creates a new user
@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()  # Parse JSON body from the request
    
    # Simple validation: check if 'name' is provided
    if 'name' not in data:
        # If no name, return an error message with HTTP status 400 (Bad Request)
        return jsonify({'error': 'Name is required'}), 400
    
    # Create new user dictionary with a unique id and the provided name
    user = {'id': len(users) + 1, 'name': data['name']}
    
    # Add the new user to our in-memory "database"
    users.append(user)
    
    # Return the created user and HTTP status 201 (Created)
    return jsonify(user), 201

