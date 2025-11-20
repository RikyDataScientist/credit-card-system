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