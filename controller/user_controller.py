from utils.database_helper import load_data, save_data
from models.user_log import User
from controller.main_page import MainController

class UserController:
    path = "database/user_info.json"

    @staticmethod
    def validate_username(username):
        if not username:
            raise ValueError("Username tidak boleh kosong")
        if len(username) < 4:
            raise ValueError("Username harus terdiri minimal 4 karakter")

    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            raise ValueError("Password harus terdiri dari 8 karakter")

    @staticmethod
    def validate_chn(cardholder_name):
        if not cardholder_name:
            raise ValueError("Nama Card Holder tidak boleh kosong")

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
            raise ValueError("Username atau Password Anda Salah")
        MainController(data_user)

        return "Login Berhasil"

    @classmethod
    def register(cls, cardholder_name, username, password):
        cls.validate_chn(cardholder_name)
        cls.validate_username(username)
        cls.validate_password(password)

        if cls.check_username_exist(username):
            raise ValueError("Username telah digunakan")

        data_user = User(cardholder_name, username, password)
        all_data = cls.load()
        all_data.append(data_user.get_data())
        cls.save(all_data)

        return "Registrasi Berhasil"
