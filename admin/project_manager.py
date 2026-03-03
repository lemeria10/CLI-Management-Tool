# from admin.file_manager import FileManager

# class ProjectManager:
#     # Manages projects.
#     def __init__(self):
#         self.file = FileManager("projects.json")

#     def create_project(self, name, owner):
#         projects = self.file.load()
#         project_id = len(projects) + 1
#         projects.append({"id": project_id, "name": name, "owner": owner})
#         self.file.save(projects)
#         print("Project created successfully!")

#     def list_projects(self, owner):
#         projects = self.file.load()
#         found = False
#         print(f"\nProjects for {owner}:")
#         for p in projects:
#             if p["owner"] == owner:
#                 print(f"ID: {p['id']} | {p['name']}")
#                 found = True
#         if not found:
#             print("No projects found.")

#     def delete_project(self, project_id):
#         projects = self.file.load()
#         updated = [p for p in projects if p["id"] != project_id]
#         if len(updated) == len(projects):
#             print("Project not found.")
#             return
#         self.file.save(updated)
#         print("Project deleted successfully!")
from admin.base_manager import BaseManager

class ProjectManager(BaseManager):
    # Manages projects.

    def __init__(self):
        super().__init__("projects.json")

    def create_project(self, name, owner):
        projects = self.load_data()
        project_id = self.generate_id(projects)

        projects.append({
            "id": project_id,
            "name": name,
            "owner": owner
        })

        self.save_data(projects)
        print("Project created successfully!")

    def list_projects(self, owner):
        projects = self.load_data()
        found = False

        print(f"\nProjects for {owner}:")

        for p in projects:
            if p["owner"] == owner:
                print(f"ID: {p['id']} | {p['name']}")
                found = True

        if not found:
            print("No projects found.")

    def delete_project(self, project_id):
        projects = self.load_data()
        updated = [p for p in projects if p["id"] != project_id]

        if len(updated) == len(projects):
            print("Project not found.")
            return

        self.save_data(updated)
        print("Project deleted successfully!")