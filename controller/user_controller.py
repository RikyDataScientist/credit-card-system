from auth.user_manager import UserManager
from models.user_log import User

class UserController:
    @staticmethod
    def login(username, password):
        UserManager.validate_username(username)
        UserManager.validate_password(password)

        data_user = UserManager.find_user(username, password)
        if not data_user:
            raise ValueError("Username atau Password Anda Salah")

        return "Login Berhasil"

    @staticmethod
    def register(cardholder_name, username, password):
        UserManager.validate_chn(cardholder_name)
        UserManager.validate_username(username)
        UserManager.validate_password(password)

        if UserManager.check_username_exist(username):
            raise ValueError("Username telah digunakan")

        data_user = User(cardholder_name, username, password)
        all_data = UserManager.load()
        all_data.append(data_user.get_data())
        UserManager.save(all_data)

        return "Registrasi Berhasil"
