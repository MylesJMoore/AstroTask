AstroTask

AstroTask is a simple web-based to-do list application built with Flask and Tailwind CSS. It allows users to add, complete, view, and delete tasks.

Features

Add tasks

Mark tasks as completed

View all tasks

Delete tasks

Installation

Prerequisites

Ensure you have Python installed on your system. If not, download and install it from python.org.

1. Clone the Repository

git clone https://github.com/yourusername/astro-task.git
cd astro-task

2. Create and Activate a Virtual Environment (Optional but Recommended)

python -m venv venv

# Activate the virtual environment:

# Windows:

venv\Scripts\activate

# Mac/Linux:

source venv/bin/activate

3. Install Dependencies

pip install flask

4. Run the Application

python app.py

You should see output like:

- Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

5. Open the Web App

Go to http://127.0.0.1:5000/ in your browser.

Usage

Add a Task: Enter a task in the input box and submit.

Mark as Completed: Click the "Complete" button.

Delete a Task: Click "Delete" to remove it.

Project Structure

astro-task/
│-- app.py # Main Flask application
│-- tasks.json # Stores task data
│-- templates/
│ ├── index.html # Frontend UI (Tailwind CSS)
│-- static/
│ ├── styles.css # Custom CSS (if needed)

License

This project is licensed under the MIT License.

Made by Myles Moore
