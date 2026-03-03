# Add this to fix import paths
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from admin.user_manager import UserManager

def test_create_list_delete_user(tmp_path):
    user_file = tmp_path / "users.json"
    manager = UserManager()
    manager.file.filename = str(user_file)
    manager.file.ensure_file_exists()

    manager.create_user("Alice")
    users = manager.load_data()
    assert len(users) == 1
    assert users[0]["username"] == "Alice"

    manager.delete_user("Alice")
    users = manager.load_data()
    assert len(users) == 0