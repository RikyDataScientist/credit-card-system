from utils.database_helper import load_data, save_data
from models.user_log import User

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
    def load(data):
        return load_data(data.path)

    @classmethod
    def save(data, data_user):
        return save_data(data.path, data_user)

    @classmethod
    def check_username_exist(data, username):
        user_data = data.load()
        return any(key["username"] == username for key in user_data)

    @classmethod
    def find_user(data, username, password=None):
        user_data = data.load()
        for key in user_data:
            if key["username"] == username:
                if key["password"] == password or password is None:
                    return key
        return None

    @classmethod
    def login(data, username, password):
        data.validate_username(username)
        data.validate_password(password)

        data_user = data.find_user(username, password)
        if not data_user:
            raise ValueError("Username atau Password Anda Salah")

        return "Login Berhasil"

    @classmethod
    def register(data, cardholder_name, username, password):
        data.validate_chn(cardholder_name)
        data.validate_username(username)
        data.validate_password(password)

        if data.check_username_exist(username):
            raise ValueError("Username telah digunakan")

        data_user = User(cardholder_name, username, password)
        all_data = data.load()
        all_data.append(data_user.get_data())
        data.save(all_data)

        return "Registrasi Berhasil"
