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
        self.setGeometry(200, 200, 1200, 700)
        self.setStyleSheet(style())

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

        main_layout.addWidget(sidebar, stretch=0)
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
        pixmap = QPixmap("asset/bank.png")
        image.setPixmap(pixmap)
        image.setFixedSize(pixmap.size())
        image.setScaledContents(True)

        username = QLabel("Card Number:")
        username.setObjectName("text")
        self.info1 = QLabel()
        self.info1.setObjectName("text")

        card_holder_name = QLabel("Card Holder Name:")
        card_holder_name.setObjectName("text")
        self.info2 = QLabel()
        self.info2.setObjectName("text")

        credit_limit = QLabel("Credit Limit:")
        credit_limit.setObjectName("text")
        self.info3 = QLabel()
        self.info3.setObjectName("text")

        remaining_credit = QLabel("Remaining Credit:")
        remaining_credit.setObjectName("text")
        self.info4 = QLabel()
        self.info4.setObjectName("text")

        bill = QLabel("User Bill:")
        bill.setObjectName("text")
        self.info5 = QLabel()
        self.info5.setObjectName("text")

        minimum_pay = QLabel("Minimum Payment:")
        minimum_pay.setObjectName("text")
        self.info6 = QLabel()
        self.info6.setObjectName("text")

        self.controller.data_changed.connect(self.update_view)
        self.update_view()

        layout = QGridLayout()

        layout.addWidget(image, 0, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(username, 1, 0)
        layout.addWidget(self.info1, 1, 1)
        layout.addWidget(card_holder_name, 2, 0)
        layout.addWidget(self.info2, 2, 1)
        layout.addWidget(credit_limit, 3, 0)
        layout.addWidget(self.info3, 3, 1)
        layout.addWidget(remaining_credit, 4, 0)
        layout.addWidget(self.info4, 4, 1)
        layout.addWidget(bill, 5, 0)
        layout.addWidget(self.info5, 5, 1)
        layout.addWidget(minimum_pay, 6, 0)
        layout.addWidget(self.info6, 6, 1)

        self.setLayout(layout)

    def update_view(self):
        self.info1.setText(str(self.controller.call_cn()))
        self.info2.setText(str(self.controller.call_chn()))
        self.info3.setText("Rp" + str(self.controller.call_cl()))
        self.info4.setText("Rp" + str(self.controller.call_rc()))
        self.info5.setText("Rp" + str(self.controller.call_bill()))
        self.info6.setText("Rp" + str(self.controller.call_mp()))

class Purchase(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        title = QLabel("Let's Purchase")
        title.setObjectName("title")

        bill = QLabel("Remaining Credit:")
        bill.setObjectName("text")
        self.info = QLabel()
        self.info.setObjectName("text")

        self.controller.data_changed.connect(self.update_view)
        self.update_view()

        self.amount_pay = QLineEdit()
        self.amount_pay.setPlaceholderText("Input Your Money")
        self.amount_pay.setObjectName("line")

        self.button = QPushButton("Purchase")
        self.button.clicked.connect(self.execute)
        self.button.setObjectName("button")

        layout = QGridLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        layout.addWidget(title, 0, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(bill, 1, 0)
        layout.addWidget(self.info, 1, 1)
        layout.addWidget(self.amount_pay, 2, 0, 1, 2)
        layout.addWidget(self.button, 3, 0, 1, 2)

        self.setLayout(layout)

    def update_view(self):
        self.info.setText("Rp" + str(self.controller.call_rc()))

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
            self.amount_pay.clear()
        except Exception as msg:
            show_error(str(msg))

class PayBill(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        title = QLabel("Let's Pay The Bill")
        title.setObjectName("title")

        bill = QLabel("Your Bill:")
        bill.setObjectName("text")
        self.info = QLabel()
        self.info.setObjectName("text")

        credit_limit = QLabel("Minimum Credit")
        credit_limit.setObjectName("text")
        self.info1 = QLabel()
        self.info1.setObjectName("text")

        self.controller.data_changed.connect(self.update_view)
        self.update_view()

        self.amount_pay = QLineEdit()
        self.amount_pay.setPlaceholderText("Input Your Money")
        self.amount_pay.setObjectName("line")

        self.button = QPushButton("Pay")
        self.button.clicked.connect(self.execute)
        self.button.setObjectName("button")

        layout = QGridLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        layout.addWidget(title, 0, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(bill, 1, 0)
        layout.addWidget(self.info, 1, 1)
        layout.addWidget(credit_limit, 2, 0)
        layout.addWidget(self.info1, 2, 1)
        layout.addWidget(self.amount_pay, 3, 0, 1, 2)
        layout.addWidget(self.button, 4, 0, 1, 2)

        self.setLayout(layout)

    def update_view(self):
        self.info.setText("Rp" + str(self.controller.call_bill()))
        self.info1.setText("Rp" + str(self.controller.call_mp()))

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
            self.amount_pay.clear()
        except Exception as msg:
            show_error(str(msg))

def style():
    return """
/* GLOBAL WIDGET */
QWidget {
    background-color: #0B1F33;
    color: #E8EEF2;
    font-family: Segoe UI;
    font-size: 14px;
}

/* SIDEBAR FRAME */
QFrame {
    background-color: #0E2A44;
}

/* GENERAL LABEL */
QLabel {
    color: #E8EEF2;
}

/* TITLE LABEL */
QLabel#title {
    font-size: 22px;
    font-weight: bold;
    color: #6BB6FF;
}

/* TEXT LABEL */
QLabel#text {
    font-size: 15px;
    color: #D9E6F2;
    background-color: transparent;
}

QLabel {
    background-color: transparent;
}

/* BUTTON STYLE */
QPushButton {
    background-color: #134A6F;
    color: white;
    padding: 10px;
    border-radius: 6px;
    border: none;
}

QPushButton:hover {
    background-color: #1C5C86;
}

QPushButton:pressed {
    background-color: #11415D;
}

/* INPUT FIELD */
QLineEdit#line {
    background-color: #0E273B;
    border: 1px solid #1E4E6F;
    border-radius: 5px;
    padding: 6px;
    color: white;
}

QLineEdit#line:focus {
    border: 1px solid #4CA3FF;
}

/* STACKED WIDGET */
QStackedWidget {
    background-color: #0B1F33;
}

/* REMOVE FRAME OUTLINE IF ANY */
QFrame {
    border: none;
}
"""
