import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from admin.base_manager import BaseManager

def test_base_manager(tmp_path):
    file_path = tmp_path / "base.json"

    # Initialize BaseManager
    bm = BaseManager(str(file_path))

    # Initially empty
    data = bm.load_data()
    assert data == []

    # Save some data (pass it to save_data)
    test_data = [{"id": 1, "name": "Sample"}]
    bm.save_data(test_data)

    # Reload and check
    loaded = bm.load_data()
    assert loaded == test_data