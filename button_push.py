from PySide6.QtWidgets import QPushButton

def button_click_checker(data):
    print("Button state:", data)

class Button_Push(QPushButton):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button")
        self.setText("Press Button to toggle")
        self.setCheckable(True)
        self.clicked.connect(button_click_checker)