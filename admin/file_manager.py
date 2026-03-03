import json
import os

class FileManager:
    
    def __init__(self, filename):
        self.filename = filename
        self.ensure_file_exists()

    def ensure_file_exists(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f)

    def load(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def save(self, data):
        try:
            with open(self.filename, "w") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print("Error saving file:", e)