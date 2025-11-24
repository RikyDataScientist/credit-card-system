from PyQt6.QtWidgets import QApplication, QStackedWidget
from gui.auth_page import Login, Register
from controller.user_controller import UserController

# --- MAIN APP TEST ---
app = QApplication([])

# Stacked widget
stack = QStackedWidget()
controller = UserController()

# Pages
login = Login(stack, controller)
signup = Register(stack, controller)

# Tambahkan ke stack
stack.addWidget(login)   # index 0
stack.addWidget(signup)  # index 1

stack.setCurrentIndex(0)

stack.show()
app.exec()