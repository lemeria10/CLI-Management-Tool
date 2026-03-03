import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from admin.project_manager import ProjectManager

def test_create_list_delete_project(tmp_path):
    project_file = tmp_path / "projects.json"
    manager = ProjectManager()
    manager.file.filename = str(project_file)
    manager.file.ensure_file_exists()

    manager.create_project("Website", "Alice")
    projects = manager.load_data()
    assert len(projects) == 1

    manager.delete_project(1)
    projects = manager.load_data()
    assert len(projects) == 0