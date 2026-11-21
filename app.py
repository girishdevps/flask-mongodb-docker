from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongofb:27017/")
db = client["devops_project"]
users = db["users"]

@app.route('/')
def home():
    return "Flask + MongoDB App Running"

@app.route('/users', methods=['GET'])
def get_users():
    data = list(users.find({}, {"_id": 0}))
    return jsonify(data)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    users.insert_one(data)
    return jsonify({"message": "User added successfully"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
