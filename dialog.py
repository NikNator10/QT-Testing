from PySide6.QtWidgets import QDialog, QDialogButtonBox
from ui_dialog import Ui_Dialog

class Dialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_box.clicked.connect(self.button_box_trigger)

    def button_box_trigger(self, button):
        std_button = self.button_box.standardButton(button)
        if std_button == QDialogButtonBox.Ok:
            if not self.fav_os_line_edit.text() == '':
                self.accept()
        if std_button == QDialogButtonBox.Save:
            print("Save")
        if std_button == QDialogButtonBox.Cancel:
            self.reject()
        if std_button == QDialogButtonBox.Open:
            print("Open")