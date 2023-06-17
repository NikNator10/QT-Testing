from PySide6.QtWidgets import QApplication
from forms import DataForm
import sys

app = QApplication(sys.argv)

datawindow = DataForm(app)
datawindow.show()

app.exec()