from PySide6.QtWidgets import QWidget, QDialog
from ui_widget import Ui_Widget
from dialog import Dialog

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Widget")

        self.dialog = Dialog()

        self.provide_information_button.clicked.connect(self.provide_info)

    def provide_info(self):
        ret = self.dialog.exec()
        if ret == QDialog.Accepted:
            self.info_label.setText(f"Your name is {self.dialog.name} & your favourite OS is {self.dialog.fav_os}")

