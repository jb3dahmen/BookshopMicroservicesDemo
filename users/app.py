# User Service
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

users = {}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    user_id = str(uuid4())
    user = {"id": user_id, **data}
    users[user_id] = user
    return jsonify(user), 201

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

if __name__ == "__main__":
    app.run(port=5002)