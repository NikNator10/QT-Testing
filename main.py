import sys
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow

app = QApplication(sys.argv)
mw = MainWindow(app)

mw.show()
app.exec()