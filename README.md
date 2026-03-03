# CLI Project Management Tool

A **simple Command-Line Interface (CLI)** to manage **Users, Projects, and Tasks** using Python.  
Data is stored in **JSON files**, and the CLI is powered by **Typer**.

---

## Features

- Create, list, and delete **users**
- Create, list, and delete **projects**
- Create, list, and complete **tasks**
- Data stored in JSON files:  
  `users.json`, `projects.json`, `tasks.json`
- Modular design with manager classes:
  - `BaseManager.py` – shared logic for file handling  
  - `FileManager.py` – read/write JSON files  
  - `UserManager.py`, `ProjectManager.py`, `TaskManager.py` – CRUD operations
- Tested with **pytest** for reliability

---

## Project Structure


CLIProjectManagementTool/
│
├─ admin/ # Manager modules
│ ├─ base_manager.py # Base class for managers
│ ├─ file_manager.py # Handles JSON files
│ ├─ user_manager.py
│ ├─ project_manager.py
│ └─ task_manager.py
│
├─ tests/ # Pytest test files
│ ├─ init.py
│ ├─ test_base_manager.py
│ ├─ test_file_manager.py
│ ├─ test_user_manager.py
│ ├─ test_project_manager.py
│ └─ test_task_manager.py
│
├─ main.py # CLI entry point
├─ users.json # Stores user data
├─ projects.json # Stores project data
├─ tasks.json # Stores task data
├─ requirements.txt # Python dependencies
└─ README.md




## Setup Instructions

### 1. Clone the repository

git clone <your-repo-url>
cd CLIProjectManagementTool
### 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows PowerShell
### 3. Install dependencies
pip install -r requirements.txt
## How to Use the CLI

Run all commands from the project root:

python3 main.py [command] [arguments]
User Commands

Create a new user:

python3 main.py create_user Alice

List all users:

python3 main.py list_users

Delete a user:

python3 main.py delete_user Alice
Project Commands

Create a project:

python3 main.py create_project "Website Redesign" Alice

List projects for a user:

python3 main.py list_projects Alice

Delete a project by ID:

python3 main.py delete_project 1
Task Commands

Create a task:

python3 main.py create_task "Design Homepage" 1 Alice Bob

List tasks for a project:

python3 main.py list_tasks 1

Mark a task as complete:

python3 main.py complete_task 1
## Running Tests

We use pytest to test all managers and file handling:

pytest -v