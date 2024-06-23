from flask import Blueprint, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

user_bp = Blueprint('user', __name__)

# MongoDB connection
client = MongoClient(os.getenv('MONGODB_URI'))
db = client.get_default_database()

@user_bp.route('/users', methods=['GET'])
def get_users():
    # Example route to fetch all users from MongoDB
    users = list(db.users.find({}, {'password': 0}))  # Exclude password field
    return jsonify({'users': users})
