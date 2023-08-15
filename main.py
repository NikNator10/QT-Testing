import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

# Create the UI - Loader
loader = QUiLoader()

# Initialize the QApplication & load UI from the file
app = QtWidgets.QApplication(sys.argv)
window = loader.load("widget.ui", None)

# Manipulate Widget like a real object
window.setWindowTitle("Basic Text-Editor")

def copy():
    window.text_edit.copy()

def paste():
    window.text_edit.paste()

def select_all():
    window.text_edit.selectAll()

# Accessing Widgets
window.copy_button.clicked.connect(copy)
window.paste_button.clicked.connect(paste)
window.select_all_button.clicked.connect(select_all)

window.show()
app.exec()

