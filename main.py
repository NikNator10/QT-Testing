from PySide6.QtWidgets import QApplication
from widget import TextEditor
import sys

app = QApplication(sys.argv)
widget = TextEditor(app)

widget.show()
app.exec()