from PyQt6.QtWidgets import QMessageBox

def show_info(msg):
    popup = QMessageBox()
    popup.setIcon(QMessageBox.Icon.Information)
    popup.setText(msg)
    popup.exec()

def show_error(msg):
    popup = QMessageBox()
    popup.setIcon(QMessageBox.Icon.Critical)
    popup.setText(msg)
    popup.exec()
