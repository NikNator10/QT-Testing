from PySide6.QtWidgets import QApplication,QMainWindow, QPushButton, QHBoxLayout, QMenuBar
from PySide6.QtCore import QSize

def button1_trigger(data):
    print("Status:", data)

def button2_trigger(data):
    print("Status:", data)

class MainButton(QPushButton):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Test")
        button1 = QPushButton("Button 1")
        button1.setCheckable(True)
        button2 = QPushButton("Button 2")
        button2.setCheckable(True)
        button1.clicked.connect(button1_trigger)
        button2.clicked.connect(button2_trigger)


        button_layout = QHBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        self.setLayout(button_layout)

