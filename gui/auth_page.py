from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget, QFrame, QVBoxLayout, QPushButton, QLineEdit, QLabel, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QFont

class Login(QWidget):
    def __init__(self, stack):
        super().__init__()
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
        link.linkActivated.connect(lambda: stack.setCurrentIndex(1))
        link.setObjectName('subtitle')
        link.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.button = QPushButton("Login")
        self.button.clicked.connect(lambda: stack.setCurrentIndex(2))
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

class SignupPage(QWidget):
    def __init__(self):
        super().__init__()
        label = QLabel("This is Signup Page", alignment=Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size:20px; color:white;")

class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        label = QLabel("This is Main Dashboard", alignment=Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size:20px; color:white;")


# --- MAIN APP TEST ---
app = QApplication([])

# Stacked widget
stack = QStackedWidget()

# Pages
login = Login(stack)
signup = SignupPage()
main = MainPage()

# Tambahkan ke stack
stack.addWidget(login)   # index 0
stack.addWidget(signup)  # index 1
stack.addWidget(main)    # index 2

stack.setCurrentIndex(0)
stack.setFixedSize(420, 520)

# --- CSS ---
app.setStyleSheet("""
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
        }

        #subtitle {
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

stack.show()
app.exec()