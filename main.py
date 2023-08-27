import sys
from PySide6.QtWidgets import QApplication
from widget import Widget

app = QApplication(sys.argv)
# Set a style to get the same experience on different operating systems
app.setStyle("Fusion")

widget = Widget()

widget.show()
app.exec()

