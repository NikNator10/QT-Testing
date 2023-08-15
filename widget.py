from PySide6.QtWidgets import QWidget, QAbstractItemView
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Basic Todo-Application")

        self.todo_list_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.add_todo_button.clicked.connect(self.add_todo)

    def add_todo(self):
        self.todo_list_widget.addItem(self.add_todo_line_edit.text())