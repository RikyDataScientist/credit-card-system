from models.main_model import MainModel
from utils.database_helper import load_data, save_data

class MainController:
    def __init__(self, user_login_data):
        self.db = "database/user_info.json"
        self.model = MainModel(user_login_data)

    def make_purchase(self, amount):
        try:
            result = self.model.purchase(amount)
            self.save_to_json()
            if result is True:
                return f"Your Rp{amount} Purchase is Success"
        except Exception as e:
            raise e

    def pay_charge(self, amount):
        try:
            result = self.model.pay(amount)
            self.save_to_json()
            if result is True:
                return f"Your Rp{amount} Repay is Success"
        except Exception as e:
            raise e

    def save_to_json(self):
        all_users = load_data(self.db)
        self.model.update()
        for index, user in enumerate(all_users):
            if (user["username"] == self.model.username) and (user["password"] == self.model.password):
                all_users[index] = self.model.user

        save_data(self.db, all_users)

    def call_cn(self):
        return self.model.card_number

    def call_chn(self):
        return self.model.chn

    def call_cl(self):
        return self.model.credit_limit

    def call_rc(self):
        return self.model.remaining_credit

    def call_bill(self):
        return self.model.bill

    def call_mp(self):
        return self.model.min_pay
