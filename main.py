from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def generate_plan(task):
    return {
        "goal": task,
        "steps": [
            "Understand the topic",
            "Practice basic problems",
            "Solve intermediate problems",
            "Revise and test yourself"
        ],
        "duration": "2 weeks"
    }

@app.route("/", methods=["GET"])
def home():
    return "AI Task Agent is running!"

@app.route("/run", methods=["POST"])
def run():
    data = request.get_json()
    task = data.get("task", "")
    
    result = generate_plan(task)
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)