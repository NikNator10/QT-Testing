from PySide6.QtWidgets import QWidget, QDialog
from ui_widget import Ui_Widget
from dialog import Dialog

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QWidget - Window")

        self.dialog = Dialog()

        self.provide_info_button.clicked.connect(self.provide_info)

    def provide_info(self):
        ret = self.dialog.exec()
        if ret == QDialog.Accepted:
            self.info_label.setText(f"Your information: Your name is {self.dialog.name_line_edit.text()} and your favourite OS is {self.dialog.combo_box.currentText()}.")
        else:
            print("Dialog rejected")
        