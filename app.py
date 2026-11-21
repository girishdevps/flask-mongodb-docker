
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongofb:27017/")
db = client["devops_project"]
scores = db["scores"]

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/score', methods=['POST'])
def save_score():
    data = request.get_json()

    if not data or "score" not in data:
        return jsonify({"error": "Score is required"}), 400

    scores.insert_one({
        "player": data.get("player", "Anonymous"),
        "score": int(data["score"])
    })

    return jsonify({"message": "Score saved"}), 201

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    data = list(scores.find({}, {"_id": 0}).sort("score", -1).limit(10))
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

