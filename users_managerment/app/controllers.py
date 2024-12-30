# filepath: /c:/Users/Admin/Desktop/aht/python-basic/users_managerment/app/controllers.py
from app.models import UserModel
from app.validators import Validator
import re

class UserController:
    def __init__(self):
        self.model = UserModel()
        self.validator = Validator()

    def list_users(self):
        users = self.model.fetch_all_users()
        print("List of users:")
        for user in users:
            print(f'{user["id"]}: {user["name"]} ({user["email"]})')

    def add_user(self, name, email, password):
        if not self.validator.validate_email(email):
            raise ValueError("Invalid email format")
        if not self.validator.validate_password(password):
            raise ValueError("Password cannot be empty")
        self.model.create_user(name, email, password)
        print("User created successfully.")

    def edit_user(self, user_id, name, email, password):
        if not self.validator.validate_email(email):
            raise ValueError("Invalid email format")
        if not self.validator.validate_password(password):
            raise ValueError("Password cannot be empty")
        self.model.update_user(user_id, name, email, password)
        print("User updated successfully.")

    def remove_user(self, user_id):
        self.model.delete_user(user_id)
        print("User deleted successfully.")

