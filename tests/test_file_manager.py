# Fix import paths
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
from admin.file_manager import FileManager

def test_file_manager_load_save(tmp_path):
    file_path = tmp_path / "data.json"

    # Initialize FileManager
    fm = FileManager(str(file_path))

    # File should exist and start empty
    data = fm.load()
    assert data == []

    # Save some data
    test_data = [{"id": 1, "name": "Test"}]
    fm.save(test_data)

    # Reload and verify
    loaded = fm.load()
    assert loaded == test_data

    # Write invalid JSON manually
    with open(file_path, "w") as f:
        f.write("{ invalid json }")

    # Load should not crash
    data = fm.load()
    assert data == []