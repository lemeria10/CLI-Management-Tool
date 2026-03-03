from admin.file_manager import FileManager

class BaseManager:
    # Parent class for all managers

    def __init__(self, filename):
        self.file = FileManager(filename)

    def load_data(self):
        return self.file.load()

    def save_data(self, data):
        self.file.save(data)

    def generate_id(self, items):
        return len(items) + 1