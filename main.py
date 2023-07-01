from PySide6.QtWidgets import QApplication
from text import Editor
from img import Img
import sys

app = QApplication(sys.argv)

text_editor = Editor(app)
text_editor.show()

img_test = Img()
img_test.show()

app.exec()