from PySide6.QtWidgets import QApplication
from forms import Widget
import sys

app = QApplication(sys.argv)
widget = Widget(app)

widget.show()
app.exec()