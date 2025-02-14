from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)
TASKS_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from the JSON file, ensuring it extracts the task list correctly."""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as f:
                data = json.load(f)
                if isinstance(data, dict) and "tasks" in data:  # Ensure it's a dictionary with "tasks"
                    return data["tasks"]
                elif isinstance(data, list):  # Fallback if old format exists
                    return data
        except json.JSONDecodeError:
            pass  # Handle corrupted JSON files
    return []

def save_tasks(tasks):
    """Ensures tasks are saved inside a dictionary with a 'tasks' key."""
    with open(TASKS_FILE, "w") as f:
        json.dump({"tasks": tasks}, f, indent=4)

@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Returns the list of tasks."""
    tasks = load_tasks()
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    """Adds a new task from JSON request."""
    if not request.is_json:
        return jsonify({"error": "Unsupported Media Type"}), 415

    data = request.get_json()
    if "text" not in data:
        return jsonify({"error": "Missing task text"}), 400

    tasks = load_tasks()
    task = {"id": len(tasks) + 1, "text": data["text"], "completed": False}
    tasks.append(task)
    save_tasks(tasks)

    return jsonify(task), 201

@app.route('/tasks', methods=['DELETE'])
def delete_task():
    """Deletes a task by ID."""
    if not request.is_json:
        return jsonify({"error": "Unsupported Media Type"}), 415

    data = request.get_json()
    if "id" not in data:
        return jsonify({"error": "Missing task ID"}), 400

    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != data["id"]]
    save_tasks(new_tasks)

    return jsonify({"message": "Task deleted"}), 200

@app.route('/complete', methods=['POST'])
def complete_task():
    """Marks a task as completed."""
    if not request.is_json:
        return jsonify({"error": "Unsupported Media Type"}), 415

    data = request.get_json()
    if "id" not in data:
        return jsonify({"error": "Missing task ID"}), 400

    tasks = load_tasks()
    for task in tasks:
        if task["id"] == data["id"]:
            task["completed"] = True

    save_tasks(tasks)
    return jsonify({"message": "Task marked as complete"}), 200

if __name__ == '__main__':
    app.run(debug=True)
