from datetime import datetime

class User:
    sequence = 0

    def __init__(self, cardholder_name, username, password, credit_limit=80000000):
        self.chn = cardholder_name
        self.username = username
        self.password = password

        User.sequence += 1
        current_datetime = datetime.now().strftime('%Y%m%d%H%M')
        self.card_number = f"25{User.sequence:02d}{current_datetime}"
        self.credit_limit = credit_limit
        self.remaining_credit = credit_limit
        self.bill = 0
        self.min_pay = 0

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
        return True

    def get_data(self):
        return {
            "username": self.username,
            "password": self.password,
            "card holder name": self.chn,
            "number card": self.card_number,
            "credit limit": self.credit_limit,
            "remaining credit": self.remaining_credit,
            "credit bill": self.bill,
            "minimum payment": self.min_pay
        }