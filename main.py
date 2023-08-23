import sys
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow

app = QApplication(sys.argv)
mainwindow = MainWindow(app)

mainwindow.show()
app.exec()