from flask import Flask, request
import json
import random

app = Flask(__name__)

def generate_plan(task):
    words = task.split()


    base_steps = [
        f"Understand the basics of {task}",
        f"Identify key concepts related to {task}",
        f"Practice tasks involving {words[0] if words else 'the topic'}",
        f"Build a small project on {task}",
        f"Revise and optimize your understanding of {task}"
    ]


    random.shuffle(base_steps)


    durations = ["1 week", "2 weeks", "3 weeks", "1 month"]
    
    return {
        "goal": task,
        "steps": base_steps[:4],
        "duration": random.choice(durations),
        "agent_note": "Plan generated dynamically based on task input"
    }


@app.route("/", methods=["GET"])
def home():
    return """A
    <h2>AI Task Automation Agent</h2>
    <form action="/run" method="post">
        <input type="text" name="task" placeholder="Enter your task" required style="width:300px;height:30px;">
        <br><br>
        <button type="submit" style="height:35px;">Run Agent</button>
    </form>
    """


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
