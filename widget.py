from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QDialog
from infodialog import Infodialog
class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200,100)
        self.setWindowTitle("External Stylesheets in Qt")
        self.dialog = Infodialog()

        button = QPushButton("Click here")
        button.clicked.connect(self.create_info_dialog)
        self.name_label = QLabel("Name: ")
        v_layout = QVBoxLayout()
        v_layout.addWidget(button)
        v_layout.addWidget(self.name_label)
        self.setLayout(v_layout)
    
    def create_info_dialog(self):
        ret = self.dialog.exec()
        if ret == QDialog.Accepted:
            self.name_label.setText(f"Name: {self.dialog.name}")
        else:
            print("Dialog rejected")

