from utils.database_helper import load_data,save_data

class UserManager:
    path = "database/user_info.json"

    @staticmethod
    def validate_username(username):
        if not username:
            raise ValueError("Username tidak boleh kosong")
        if len(username) <= 4:
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
