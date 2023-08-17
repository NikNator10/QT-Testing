from PySide6.QtWidgets import QWidget, QDialog
from ui_widget import Ui_Widget
from dialog import Dialog

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QDialog - Demo: Provided Info")

        self.dialog = Dialog()
        
        self.provide_info_button.clicked.connect(self.provide_info)

    def provide_info(self):
        ret = self.dialog.exec()
        if ret == QDialog.Accepted:
            self.list_widget.addItem(self.dialog.info)
            print("Dialog accpeted")
        else:
            print("Dialog rejected")
        