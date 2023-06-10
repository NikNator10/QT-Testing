from PySide6.QtWidgets import QApplication, QPushButton, QWidget ,QHBoxLayout

def button1_click(data):
    print("Button 1 state:", data)

def button2_click(data):
    print("Button 2 state:", data)

class Button_Push(QPushButton):
    def __init__(self):
        super().__init__()
        button1 = QPushButton("Button 1")
        button1.setCheckable(True)
        button1.clicked.connect(button1_click)
        button2 = QPushButton ("Button 2")
        button2.setCheckable(True)
        button2.clicked.connect(button2_click)
        button_layout = QHBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        self.setLayout(button_layout)