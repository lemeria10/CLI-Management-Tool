
from admin.base_manager import BaseManager

class UserManager(BaseManager):
    # Manages users.

    def __init__(self):
        super().__init__("users.json")

    def create_user(self, username):
        users = self.load_data()

        # Check if user already exists
        if any(u["username"] == username for u in users):
            print("User already exists.")
            return

        users.append({
            "username": username
        })

        self.save_data(users)
        print("User created successfully!")

    def list_users(self):
        users = self.load_data()

        if not users:
            print("No users found.")
            return

        print("\nUsers:")
        for u in users:
            print("-", u["username"])

    def delete_user(self, username):
        users = self.load_data()
        updated = [u for u in users if u["username"] != username]

        if len(updated) == len(users):
            print("User not found.")
            return

        self.save_data(updated)
        print("User deleted successfully!")