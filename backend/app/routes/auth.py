from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os

load_dotenv()

auth_bp = Blueprint('auth', __name__)

# MongoDB connection
client = MongoClient(os.getenv('MONGODB_URI'))
db = client.get_default_database()

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if username already exists
    if db.users.find_one({'username': username}):
        return jsonify({'error': 'Username already exists'}), 400

    # Hash the password
    hashed_password = generate_password_hash(password, method='sha256')

    # Insert user into database
    db.users.insert_one({
        'username': username,
        'password': hashed_password
    })

    return jsonify({'message': 'User registered successfully'})

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Find user by username
    user = db.users.find_one({'username': username})

    if not user or not check_password_hash(user['password'], password):
        return jsonify({'error': 'Invalid username or password'}), 401

    # Implement JWT token generation here if needed

    return jsonify({'message': 'Login successful'})
