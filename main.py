import typer
from admin.user_manager import UserManager
from admin.project_manager import ProjectManager
from admin.task_manager import TaskManager

app = typer.Typer()  # Main Typer app

# Initialize managers
user_mgr = UserManager()
proj_mgr = ProjectManager()
task_mgr = TaskManager()

# ---------------- User Commands ----------------
@app.command(name="create_user")
def create_user(username: str):
    """Create a new user."""
    user_mgr.create_user(username)

@app.command(name="list_users")
def list_users():
    """List all users."""
    user_mgr.list_users()

@app.command(name="delete_user")
def delete_user(username: str):
    
    user_mgr.delete_user(username)

# ---------------- Project Commands ----------------
@app.command(name="create_project")
def create_project(name: str, owner: str):
    
    proj_mgr.create_project(name, owner)

@app.command(name="list_projects")
def list_projects(owner: str):
    
    proj_mgr.list_projects(owner)

@app.command(name="delete_project")
def delete_project(project_id: int):
    
    proj_mgr.delete_project(project_id)

# ---------------- Task Commands ----------------
@app.command(name="create_task")
def create_task(name: str, project_id: int, contributors: list[str]):
    
    task_mgr.create_task(name, project_id, contributors)

@app.command(name="list_tasks")
def list_tasks(project_id: int):
    
    task_mgr.list_tasks(project_id)

@app.command(name="complete_task")
def complete_task(task_id: int):
   
    task_mgr.mark_complete(task_id)

if __name__ == "__main__":
    app()