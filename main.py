from PySide6.QtWidgets import QApplication
from functions import MainWindow
import sys

app = QApplication(sys.argv)
mw = MainWindow(app)

mw.show()
app.exec()

