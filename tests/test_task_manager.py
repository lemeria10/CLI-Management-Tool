# Fix import paths
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from admin.task_manager import TaskManager

def test_create_list_complete_task(tmp_path):
    task_file = tmp_path / "tasks.json"

    # Initialize manager
    manager = TaskManager()
    manager.file.filename = str(task_file)
    manager.file.ensure_file_exists()

    # 1️⃣ Create task
    manager.create_task("Design UI", 1, ["Alice"])
    tasks = manager.load_data()
    assert len(tasks) == 1
    assert tasks[0]["name"] == "Design UI"
    assert not tasks[0]["completed"]

    # 2️⃣ Mark task complete
    manager.mark_complete(1)
    tasks = manager.load_data()
    assert tasks[0]["completed"] is True

    # 3️⃣ List tasks (ensure no error)
    manager.list_tasks(1)