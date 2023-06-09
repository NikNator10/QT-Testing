from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider
from button_push import Button_Push
from slider_state import Slider_State
import sys

app = QApplication(sys.argv)
button = Button_Push()
slider = Slider_State()
#slider = QSlider(Qt.Horizontal) # Wie kann ich das in die Klasse integrieren?

button.show()
slider.show()
app.exec()