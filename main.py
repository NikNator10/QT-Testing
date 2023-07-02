from PySide6.QtWidgets import QApplication
from layout import GridLayout
import sys

app = QApplication(sys.argv)
gridlayout = GridLayout()

gridlayout.show()
app.exec()