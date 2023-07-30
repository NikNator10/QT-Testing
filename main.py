from PySide6.QtWidgets import QApplication
from widget import Todo
import sys

app = QApplication(sys.argv)
todo_app = Todo(app)

todo_app.show()
app.exec()