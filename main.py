from PySide6.QtWidgets import QApplication
from widget import Editor
import sys

app = QApplication(sys.argv)
widget = Editor(app)

widget.show()
app.exec()