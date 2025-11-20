from utils.database_helper import load_data, save_data

class MainModel:
    def __init__(self, data):
        self.user = data

        self.username = data["username"]
        self.password = data["password"]
        self.chn = data["card holder name"]
        self.card_number = data["number card"]
        self.credit_limit = data["credit limit"]
        self.remaining_credit = data["remaining credit"]
        self.bill = data["credit bill"]
        self.min_pay = data["minimum payment"]

    def update_minimum_pay(self):
        self.min_pay = self.bill * 0.1

    def purchase(self, amount):
        if self.remaining_credit < amount:
            return False
        self.bill += amount
        self.remaining_credit -= amount
        self.update_minimum_pay()
        return True

    def pay(self, amount):
        if amount <= 0:
            return False
        self.bill -= amount
        if self.bill < 0:
            self.bill = 0
        self.remaining_credit = self.credit_limit - self.bill
        self.update_minimum_pay()
        return True

    def update(self):
        self.user.update({
            "remaining credit": self.remaining_credit,
            "credit bill": self.bill,
            "minimum payment": self.min_pay
        })
