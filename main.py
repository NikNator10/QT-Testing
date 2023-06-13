from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt
from button_push import MainButton
from sliderwindow import SliderMainWindow
import sys

app = QApplication(sys.argv)
mainbutton = MainButton(app)
sliderwindow = SliderMainWindow(app)

sliderwindow.show()
mainbutton.show()
app.exec()
