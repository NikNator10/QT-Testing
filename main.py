from PySide6.QtWidgets import QApplication
from widget import Combo
import sys

app = QApplication(sys.argv)
combobox = Combo()

combobox.show()
app.exec()