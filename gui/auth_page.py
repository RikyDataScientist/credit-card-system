from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget, QFrame, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QFont

class Login(QWidget):
    def __init__(self, stack, controller):
        super().__init__()
        self.stack = stack
        self.controller = controller

        title = QLabel('Login in to HimBank')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setObjectName('title')

        self.username = QLineEdit()
        self.username.setPlaceholderText('Username')
        self.username.setObjectName('inputtext')

        self.password = QLineEdit()
        self.password.setPlaceholderText('Password')
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setObjectName('inputtext')

        link = QLabel()
        link.setText(
            "<span style='color:white;'>Don't have an account?</span> "
            "<a href='signup' style='color:#4da3ff;'>Click here</a>"
        )
        link.setTextFormat(Qt.TextFormat.RichText)
        link.setOpenExternalLinks(False)
        link.linkActivated.connect(lambda: self.stack.setCurrentIndex(1))
        link.setObjectName('subtitle')
        link.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.button = QPushButton("Login")
        self.button.clicked.connect(self.execute)
        self.button.setObjectName('button')

        frame = QFrame()
        frame.setObjectName('card')
        frameLayout = QVBoxLayout(frame)

        frameLayout.addWidget(title)
        frameLayout.addSpacing(30)
        frameLayout.addWidget(self.username)
        frameLayout.addWidget(self.password)
        frameLayout.addWidget(link)
        frameLayout.addSpacing(20)
        frameLayout.addWidget(self.button)

        mainLayout = QVBoxLayout(self)
        mainLayout.addStretch()
        mainLayout.addWidget(frame)
        mainLayout.addStretch()

    def execute(self):
        username = self.username.text()
        password = self.password.text()

        try:
            message = self.controller.login(username, password)
            print(message)
            self.stack.setCurrentIndex(2)
        except Exception as msg:
            self.show_error(str(msg))

    def show_error(self, msg):
        popup = QMessageBox()
        popup.setIcon(QMessageBox.Icon.Critical)
        popup.setText(msg)
        popup.exec()


class Register(QWidget):
    def __init__(self, stack, controller):
        super().__init__()
        self.stack = stack
        self.controller = controller

        title = QLabel('Register Account')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setObjectName('title')

        self.chn = QLineEdit()
        self.chn.setPlaceholderText('Card Holder Name')
        self.chn.setObjectName('inputtext')

        self.username = QLineEdit()
        self.username.setPlaceholderText('Username')
        self.username.setObjectName('inputtext')

        self.password = QLineEdit()
        self.password.setPlaceholderText('Password')
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setObjectName('inputtext')

        link = QLabel()
        link.setText(
            "<span style='color:white;'>Do you have an account?</span> "
            "<a href='signup' style='color:#4da3ff;'>Click here</a>"
        )
        link.setTextFormat(Qt.TextFormat.RichText)
        link.setOpenExternalLinks(False)
        link.linkActivated.connect(lambda: self.stack.setCurrentIndex(0))
        link.setObjectName('subtitle')
        link.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.button = QPushButton("Register")
        self.button.clicked.connect(self.execute)
        self.button.setObjectName('button')

        frame = QFrame()
        frame.setObjectName('card')
        frameLayout = QVBoxLayout(frame)

        frameLayout.addWidget(title)
        frameLayout.addSpacing(30)
        frameLayout.addWidget(self.chn)
        frameLayout.addWidget(self.username)
        frameLayout.addWidget(self.password)
        frameLayout.addWidget(link)
        frameLayout.addSpacing(20)
        frameLayout.addWidget(self.button)

        mainLayout = QVBoxLayout(self)
        mainLayout.addStretch()
        mainLayout.addWidget(frame)
        mainLayout.addStretch()

    def execute(self):
        cardholder_name = self.chn.text()
        username = self.username.text()
        password = self.password.text()

        try:
            message = self.controller.register(cardholder_name, username, password)
            print(message)
            self.stack.setCurrentIndex(0)
        except Exception as msg:
            self.show_error(str(msg))

    def show_error(self, msg):
        popup = QMessageBox()
        popup.setIcon(QMessageBox.Icon.Critical)
        popup.setText(msg)
        popup.exec()

class MainPage(QWidget):
    def __init__(self, stack):
        super().__init__()
        label = QLabel("This is Main Dashboard", alignment=Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size:20px; color:white;")
