from utils.database_helper import load_data, save_data
from models.user_log import User

class UserController:
    path = "database/user_info.json"

    @staticmethod
    def validate_username(username):
        if not username:
            raise ValueError("Username cannot be empty")
        if len(username) < 4:
            raise ValueError("Usernames must consist of at least 4 characters")

    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            raise ValueError("Passwords must consist of at least 8 characters")

    @staticmethod
    def validate_chn(cardholder_name):
        if not cardholder_name:
            raise ValueError("Card Holder Name cannot be empty")

    @classmethod
    def load(cls):
        return load_data(cls.path)

    @classmethod
    def save(cls, data_user):
        return save_data(cls.path, data_user)

    @classmethod
    def check_username_exist(cls, username):
        user_data = cls.load()
        return any(key["username"] == username for key in user_data)

    @classmethod
    def find_user(cls, username, password=None):
        user_data = cls.load()
        for key in user_data:
            if key["username"] == username:
                if key["password"] == password or password is None:
                    return key
        return None

    @classmethod
    def login(cls, username, password):
        cls.validate_username(username)
        cls.validate_password(password)

        data_user = cls.find_user(username, password)
        if not data_user:
            raise ValueError("Your username or password is incorrect.")
        return "Login Success", data_user

    @classmethod
    def register(cls, cardholder_name, username, password):
        cls.validate_chn(cardholder_name)
        cls.validate_username(username)
        cls.validate_password(password)

        if cls.check_username_exist(username):
            raise ValueError("The username already exists")

        data_user = User(cardholder_name, username, password)
        all_data = cls.load()
        all_data.append(data_user.get_data())
        cls.save(all_data)

        return "Registration Success"
