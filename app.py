from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)
TASKS_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from the JSON file or returns an empty list if file doesn't exist."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Saves tasks to the JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET', 'POST', 'DELETE'])
def tasks():
    tasks = load_tasks()
    
    if request.method == 'POST':
        data = request.json
        task = {"id": len(tasks) + 1, "text": data["text"], "completed": False}
        tasks.append(task)
        save_tasks(tasks)
        return jsonify(task)
    
    elif request.method == 'DELETE':
        task_id = request.json.get("id")
        tasks = [task for task in tasks if task["id"] != task_id]
        save_tasks(tasks)
        return jsonify({"message": "Task deleted"})
    
    return jsonify(tasks)

@app.route('/complete', methods=['POST'])
def complete_task():
    tasks = load_tasks()
    task_id = request.json.get("id")
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
    save_tasks(tasks)
    return jsonify({"message": "Task marked as complete"})

if __name__ == '__main__':
    app.run(debug=True)
