from PySide6.QtWidgets import QApplication
from widget import Widget
import sys

app = QApplication()

widget = Widget()
widget.show()

app.exec()