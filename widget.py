from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Styles in Qt")

        self.button.clicked.connect(self.button_clicked)
        
    def button_clicked(self):
        print("Button clicked")