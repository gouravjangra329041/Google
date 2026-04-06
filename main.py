from flask import Flask, request
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

# Home page with simple UI
@app.route("/", methods=["GET"])
def home():
    return """
    <h2>AI Task Automation Agent</h2>
    <form action="/run" method="post">
        <input type="text" name="task" placeholder="Enter your task" required style="width:300px;height:30px;">
        <br><br>
        <button type="submit" style="height:35px;">Run Agent</button>
    </form>
    """

# Run agent and show output
@app.route("/run", methods=["POST"])
def run():
    task = request.form.get("task")

    result = generate_plan(task)

    return f"""
    <h3>Result:</h3>
    <pre>{json.dumps(result, indent=4)}</pre>
    <br><a href="/">Go Back</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
