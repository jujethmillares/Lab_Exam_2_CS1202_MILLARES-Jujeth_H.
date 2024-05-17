import os
from datetime import datetime

class UserManager:
    def __init__(self):
        self.user_data = {}
        self.user_folder = "user_data"
        self.user_file = self.generate_user_file_name()
        self.ensure_user_folder_exists()
        self.load_users()

    def generate_user_file_name(self):
        today = datetime.now().strftime("%Y-%m-%d")
        return os.path.join(self.user_folder, f"users_{today}.txt")

    def ensure_user_folder_exists(self):
        if not os.path.exists(self.user_folder):
            os.makedirs(self.user_folder)   

    def load_users(self):
        if os.path.exists(self.user_file):
            with open(self.user_file, "r") as file:
                for line in file:
                    username, password = line.strip().split(",")
                    self.user_data[username] = password

    def save_users(self):
        with open(self.user_file, "w") as file:
            for username, password in self.user_data.items():
                file.write(f"{username},{password}\n")

    def validate_username(self, username):
        return username in self.user_data

    def validate_password(self, username, password):
        return self.user_data.get(username) == password

    def register(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if not self.validate_username(username):
            self.user_data[username] = password
            self.save_users()
            return "Registration successful."
        else:
            return "Username already exists."

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if self.validate_username(username):
            if self.validate_password(username, password):
                return "Login successful."
            else:
                return "Incorrect password."
        else:
            return "Username does not exist."
