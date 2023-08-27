from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Stylesheets")

        self.setStyleSheet("QPushButton{color: red; background-color: blue;};QLineEdit{color: red; background-color: green;}")
        self.line_edit.setStyleSheet("color: red; background-color: green;")
