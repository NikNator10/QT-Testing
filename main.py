from PySide6.QtWidgets import QApplication
from widget import Edit
import sys

app = QApplication(sys.argv)
widget = Edit()

widget.show()
app.exec()