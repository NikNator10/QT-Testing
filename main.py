import sys
from PySide6.QtWidgets import QApplication
from widget import Widget

app = QApplication(sys.argv)
widget = Widget()

with open("styles/style.css", "r") as file:
    style = file.read()
    app.setStyleSheet(style)

widget.show()
app.exec()
