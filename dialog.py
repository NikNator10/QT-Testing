from PySide6.QtWidgets import QDialog
from ui_dialog import Ui_Dialog

class Dialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QDialog - Demo: Enter input")


        self.ok_button.clicked.connect(self.ok)
        self.cancel_button.clicked.connect(self.cancel)

    def ok(self):
        if not self.line_edit.text() == '':
            self.info = self.line_edit.text()
            self.accept()

    def cancel(self):
        self.reject()