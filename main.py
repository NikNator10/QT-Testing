import sys
from PySide6.QtWidgets import QApplication
from mainwindow import Mainwindow

app = QApplication(sys.argv)
mainwindow = Mainwindow(app)

mainwindow.show()
app.exec()