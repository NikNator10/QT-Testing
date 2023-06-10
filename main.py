from PySide6.QtWidgets import QApplication
from slider_state import Slider_State
from button_push import Button_Push
from mainwindow import MainWindow
import sys

app = QApplication()

button = Button_Push()
slider = Slider_State()
mainwindow = MainWindow(app)

mainwindow.show()
button.show()
slider.show()
app.exec()