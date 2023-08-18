from PySide6.QtWidgets import QDialog, QDialogButtonBox
from ui_dialog import Ui_Dialog

class Dialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QDialog - Window")

        self.button_box.clicked.connect(self.button_box_trigger)
    
    def button_box_trigger(self, button):
        self.std_button = self.button_box.standardButton(button)
        if self.std_button == QDialogButtonBox.Ok:
            if not self.name_line_edit.text() == '':
                self.accept()
        elif self.std_button == QDialogButtonBox.Save:
            print("Save")
        elif self.std_button == QDialogButtonBox.Open:
            print("Open")
        elif self.std_button == QDialogButtonBox.Cancel:
            self.reject()
        else:
            print("Other buttons pressed")

