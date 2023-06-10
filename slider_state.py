from PySide6.QtWidgets import QSlider

def slider_value(data):
    print("Slider changed to", data)

class Slider_State(QSlider):
    def __init__(self):
        super().__init__()
        self.setMinimum(1)
        self.setMaximum(100)
        self.setValue(25)
        self.valueChanged.connect(slider_value)
