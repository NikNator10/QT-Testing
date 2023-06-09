from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider
from button_push import Button_Push
from slider_state import Slider_State
from mainwindow import MainWindow
import sys

app = QApplication(sys.argv)
button = Button_Push()
slider = Slider_State()
mainwindow = MainWindow(app)
#slider = QSlider(Qt.Horizontal) # Wie kann ich das in die Klasse integrieren?

button.show()
slider.show()
mainwindow.show()
app.exec()