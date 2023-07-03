from PySide6.QtWidgets import QApplication
from grid import GridLayout
import sys

app = QApplication(sys.argv)
grid_layout = GridLayout(app)

grid_layout.show()
app.exec()