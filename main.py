from PySide6.QtWidgets import QApplication
from widget import Tab
import sys

app = QApplication(sys.argv)
tab_app = Tab()

tab_app.show()
app.exec()