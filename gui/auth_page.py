from PyQt6.QtWidgets import QWidget, QFrame, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt6.QtCore import Qt
from gui.main_page import Dashboard
from controller.main_page import MainController
from utils.info_helper import show_info, show_error
class Login(QWidget):
    def __init__(self, stack, controller):
        super().__init__()
        self.stack = stack
        self.controller = controller
        self.setFixedSize(420, 520)
        self.setStyleSheet("""
        QWidget {
            background-color: #0d1117;
            color: #c9d1d9;
            font-family: 'Segoe UI';
        }

        #card {
            background-color: #161b22;
            border: 1px solid #1f2937;
            border-radius: 18px;
            padding: 35px;
        }

        #title {
            font-size: 28px;
            font-weight: bold;
            color: #58a6ff;
            margin-bottom: 5px;
            border-radius: 18px;
            padding: 12px;
        }

        #subtitle {
            background-color: #161b22;
            font-size: 14px;
            color: #8b949e;
            margin-bottom: 20px;
        }

        #inputtext {
            background-color: #0d1117;
            border: 2px solid #30363d;
            padding: 12px;
            border-radius: 10px;
            font-size: 15px;
            margin-bottom: 18px;
            color: #c9d1d9;
        }

        #inputtext:focus {
            border: 2px solid #58a6ff;
            background-color: #0c162d;
        }

        #button {
            background-color: #238636;
            color: white;
            padding: 12px;
            border-radius: 10px;
            font-size: 16px;
        }

        #button:hover {
            background-color: #2ea043;
        }

        #button:pressed {
            background-color: #196c2e;
        }
        """)

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
        username = self.username.text().strip()
        password = self.password.text().strip()

        try:
            message, data = self.controller.login(username, password)
            show_info(str(message))

            main_page = MainController(data)
            dashboard = Dashboard(main_page)
            self.stack.addWidget(dashboard)
            self.stack.setCurrentIndex(2)

        except Exception as msg:
            show_error(str(msg))


class Register(QWidget):
    def __init__(self, stack, controller):
        super().__init__()
        self.stack = stack
        self.controller = controller
        self.setFixedSize(420, 520)
        self.setStyleSheet("""
        QWidget {
            background-color: #0d1117;
            color: #c9d1d9;
            font-family: 'Segoe UI';
        }

        #card {
            background-color: #161b22;
            border: 1px solid #1f2937;
            border-radius: 18px;
            padding: 35px;
        }

        #title {
            font-size: 28px;
            font-weight: bold;
            color: #58a6ff;
            margin-bottom: 5px;
            border-radius: 18px;
            padding: 12px;
        }

        #subtitle {
            background-color: #161b22;
            font-size: 14px;
            color: #8b949e;
            margin-bottom: 20px;
        }

        #inputtext {
            background-color: #0d1117;
            border: 2px solid #30363d;
            padding: 12px;
            border-radius: 10px;
            font-size: 15px;
            margin-bottom: 18px;
            color: #c9d1d9;
        }

        #inputtext:focus {
            border: 2px solid #58a6ff;
            background-color: #0c162d;
        }

        #button {
            background-color: #238636;
            color: white;
            padding: 12px;
            border-radius: 10px;
            font-size: 16px;
        }

        #button:hover {
            background-color: #2ea043;
        }

        #button:pressed {
            background-color: #196c2e;
        }
        """)

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
        cardholder_name = self.chn.text().strip().title()
        username = self.username.text().strip()
        password = self.password.text().strip()

        try:
            message = self.controller.register(cardholder_name, username, password)
            show_info(str(message))
            self.stack.setCurrentIndex(0)

        except Exception as msg:
            show_error(str(msg))
