from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QPushButton,
    QLineEdit,
    QStackedWidget,
    QLabel,
    QFrame,
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from utils.info_helper import show_info, show_error


class Dashboard(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Bank Craft")
        self.setFixedSize(800, 500)

        main_layout = QHBoxLayout(self)

        sidebar = QFrame()
        sidebar.setStyleSheet("background-color: #002D44;")
        sidebar.setFixedWidth(200)

        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(10, 10, 10, 10)
        sidebar_layout.setSpacing(25)

        btn_home = QPushButton("Home")
        btn_purchase = QPushButton("Purchase")
        btn_pay = QPushButton("Pay")

        for btn in (btn_home, btn_purchase, btn_pay):
            btn.setStyleSheet(
                """
                QPushButton {
                    background-color: #004A6E;
                    color: white;
                    padding: 10px;
                    border-radius: 5px;
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: #005C85;
                }
            """
            )
            sidebar_layout.addWidget(btn)

        sidebar_layout.addStretch()

        self.stack = QStackedWidget()

        page1 = MainPage(self.controller)
        page2 = Purchase(self.controller)
        page3 = PayBill(self.controller)

        self.stack.addWidget(page1)
        self.stack.addWidget(page2)
        self.stack.addWidget(page3)

        main_layout.addWidget(sidebar)
        main_layout.addWidget(self.stack, stretch=1)

        btn_home.clicked.connect(lambda: self.switch_page(0))
        btn_purchase.clicked.connect(lambda: self.switch_page(1))
        btn_pay.clicked.connect(lambda: self.switch_page(2))


    def switch_page(self, index):
        self.stack.setCurrentIndex(index)


class MainPage(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        image = QLabel()
        pixmap = QPixmap("bank.png")
        image.setPixmap(pixmap)
        image.setFixedSize(pixmap.size())
        image.setScaledContents(True)

        username = QLabel("Card Number:")
        info1 = QLabel(str(self.controller.call_cn()))

        card_holder_name = QLabel("Card Holder Name:")
        info2 = QLabel(str(self.controller.call_chn()))

        remaining_credit = QLabel("Remaining Credit:")
        info3 = QLabel("Rp" + str(self.controller.call_rc()))

        layout = QGridLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(0, 20, 0, 0)
        layout.setRowStretch(0, 0)
        layout.setRowStretch(1, 1)

        layout.addWidget(image, 0, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(username, 1, 0)
        layout.addWidget(info1, 1, 1)
        layout.addWidget(card_holder_name, 2, 0)
        layout.addWidget(info2, 2, 1)
        layout.addWidget(remaining_credit, 3, 0)
        layout.addWidget(info3, 3, 1)

        self.setLayout(layout)

class Purchase(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        title = QLabel("Let's Purchase")

        bill = QLabel("Remaining Credit:")
        info = QLabel("Rp" + str(self.controller.call_rc()))

        self.amount_pay = QLineEdit()
        self.amount_pay.setPlaceholderText("Input Your Money")

        self.button = QPushButton("Purchase")
        self.button.clicked.connect(self.execute)

        layout = QGridLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        layout.addWidget(title, 0, 0, 1, 2)
        layout.addWidget(bill, 1, 0)
        layout.addWidget(info, 1, 1)
        layout.addWidget(self.amount_pay, 2, 0, 1, 2)
        layout.addWidget(self.button, 3, 0, 1, 2)

        self.setLayout(layout)

    def execute(self):
        amount = self.amount_pay.text().strip()

        if amount == "":
            show_error("Input cannot be empty.")
            return

        if not amount.isdigit():
            show_error("Only numbers can be entered")
            return

        amount = int(amount)

        try:
            msg = self.controller.make_purchase(amount)
            show_info(msg)
        except Exception as msg:
            show_error(msg)

class PayBill(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        title = QLabel("Let's Pay The Bill")

        bill = QLabel("Your Bill:")
        info = QLabel("Rp" + str(self.controller.call_bill()))

        credit_limit = QLabel("Minimum Credit")
        info1 = QLabel("Rp" + str(self.controller.call_mp()))

        self.amount_pay = QLineEdit()
        self.amount_pay.setPlaceholderText("Input Your Money")

        self.button = QPushButton("Pay")
        self.button.clicked.connect(self.execute)

        layout = QGridLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        layout.addWidget(title, 0, 0, 1, 2)
        layout.addWidget(bill, 1, 0)
        layout.addWidget(info, 1, 1)
        layout.addWidget(credit_limit, 2, 0)
        layout.addWidget(info1, 2, 1)
        layout.addWidget(self.amount_pay, 3, 0, 1, 2)
        layout.addWidget(self.button, 4, 0, 1, 2)

        self.setLayout(layout)

    def execute(self):
        amount = self.amount_pay.text().strip()

        if amount == "":
            show_error("Input cannot be empty.")
            return

        if not amount.isdigit():
            show_error("Only numbers can be entered")
            return

        amount = int(amount)

        try:
            msg = self.controller.pay_charge(amount)
            show_info(msg)
        except Exception as msg:
            show_error(msg)
