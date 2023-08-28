from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Stylesheets & Palette in Qt")
        
        # You need this if you want to see the background color
        self.label_1.setAutoFillBackground(True)
        self.label_2.setAutoFillBackground(True)
        self.label_3.setAutoFillBackground(True)
        self.label_4.setAutoFillBackground(True)

        self.setStyleSheet("QPushButton{ color: red; background-color: grey;}")
        self.line_edit.setStyleSheet("QLineEdit{ color: blue; background-color: red}")

        palette_green_blue = QPalette()
        palette_green_blue.setColor(QPalette.Window, Qt.green)
        palette_green_blue.setColor(QPalette.WindowText, Qt.blue)
        
        palette_yellow_red = QPalette()
        palette_yellow_red.setColor(QPalette.Window, Qt.yellow)
        palette_yellow_red.setColor(QPalette.WindowText, Qt.red)

        self.label_1.setPalette(palette_green_blue)
        self.label_2.setPalette(palette_yellow_red)

        # Gets the palette from another label
        self.label_3.setPalette(self.label_1.palette())
        self.label_4.setPalette(self.label_2.palette())