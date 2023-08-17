from PySide6.QtWidgets import QDialog
from ui_dialog import Ui_Dialog

class Dialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Dialog")

        self.fav_os_combo_box.addItem("Linux")
        self.fav_os_combo_box.addItem("Windows")
        self.fav_os_combo_box.addItem("MacOS")
        self.ok_button.clicked.connect(self.ok)
        self.cancel_button.clicked.connect(self.cancel)

    def ok(self):
        if not self.name_line_edit.text() == '':
            self.name = self.name_line_edit.text()
            self.fav_os = self.fav_os_combo_box.currentText()
            self.accept()
            print("Dialog accpeted")
    def cancel(self):
       self.reject()
       print("Dialog rejected")
