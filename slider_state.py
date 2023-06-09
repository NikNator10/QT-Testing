from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSlider

def slider_checker(data):
    print("Slider vaule:", data)

class Slider_State(QSlider):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slider")
        self.setMinimum(1)
        self.setMaximum(100)
        self.setValue(25)
        self.valueChanged.connect(slider_checker)
