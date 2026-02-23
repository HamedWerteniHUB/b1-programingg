import json
import os

class UserStore:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, "r") as f:
            try:
                return json.load(f)
            except:
                return []

    def save(self, users):
        with open(self.file_path, "w") as f:
            json.dump(users, f, indent=4)

    def find_by_id(self, user_id):
        users = self.load()
        for user in users:
            if user["id"] == user_id:
                return user
        return None

    def get_next_id(self):
        users = self.load()
        if not users:
            return 1
        return max(user["id"] for user in users) + 1

    def update_user(self, user_id, updated_data):
        users = self.load()
        for user in users:
            if user["id"] == user_id:
                user.update(updated_data)
                self.save(users)
                return True
        return False

    def delete_user(self, user_id):
        users = self.load()
        for user in users:
            if user["id"] == user_id:
                users.remove(user)
                self.save(users)
                return True
        return False