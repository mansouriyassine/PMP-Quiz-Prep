from flask import Blueprint, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

quiz_bp = Blueprint('quiz', __name__)

# MongoDB connection
client = MongoClient(os.getenv('MONGODB_URI'))
db = client.get_default_database()

@quiz_bp.route('/quiz', methods=['GET'])
def get_quiz():
    # Example route to fetch quiz data from MongoDB
    quiz_data = list(db.quizzes.find())
    return jsonify({'quizzes': quiz_data})
