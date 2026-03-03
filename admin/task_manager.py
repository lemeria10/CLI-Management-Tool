# from admin.file_manager import FileManager

# class TaskManager:
#     # Manages tasks.
#     def __init__(self):
#         self.file = FileManager("tasks.json")

#     def create_task(self, name, project_id, contributors):
#         tasks = self.file.load()
#         task_id = len(tasks) + 1
#         tasks.append({
#             "id": task_id,
#             "project_id": project_id,
#             "name": name,
#             "completed": False,
#             "contributors": contributors
#         })
#         self.file.save(tasks)
#         print("Task created successfully!")

#     def list_tasks(self, project_id):
#         tasks = self.file.load()
#         found = False
#         print(f"\nTasks for Project {project_id}:")
#         for t in tasks:
#             if t["project_id"] == project_id:
#                 status = "Done" if t["completed"] else "Not Done"
#                 print(f"ID: {t['id']} | {t['name']} | {status}")
#                 print("Contributors:", ", ".join(t["contributors"]))
#                 print("---------------------")
#                 found = True
#         if not found:
#             print("No tasks found.")

#     def mark_complete(self, task_id):
#         tasks = self.file.load()
#         for t in tasks:
#             if t["id"] == task_id:
#                 t["completed"] = True
#                 self.file.save(tasks)
#                 print("Task marked complete!")
#                 return
#         print("Task not found.")
from admin.base_manager import BaseManager

class TaskManager(BaseManager):
    # Manages tasks.

    def __init__(self):
        super().__init__("tasks.json")

    def create_task(self, name, project_id, contributors):
        tasks = self.load_data()
        task_id = self.generate_id(tasks)

        tasks.append({
            "id": task_id,
            "project_id": project_id,
            "name": name,
            "completed": False,
            "contributors": contributors
        })

        self.save_data(tasks)
        print("Task created successfully!")

    def list_tasks(self, project_id):
        tasks = self.load_data()
        found = False

        print(f"\nTasks for Project {project_id}:")

        for t in tasks:
            if t["project_id"] == project_id:
                status = "Done" if t["completed"] else "Not Done"
                print(f"ID: {t['id']} | {t['name']} | {status}")
                print("Contributors:", ", ".join(t["contributors"]))
                print("---------------------")
                found = True

        if not found:
            print("No tasks found.")

    def mark_complete(self, task_id):
        tasks = self.load_data()

        for t in tasks:
            if t["id"] == task_id:
                t["completed"] = True
                self.save_data(tasks)
                print("Task marked complete!")
                return

        print("Task not found.")