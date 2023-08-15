from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Basic Text-Editor")

        self.select_all_button.clicked.connect(self.select_all)
        self.copy_button.clicked.connect(self.copy)
        self.paste_button.clicked.connect(self.paste)
        self.undo_button.clicked.connect(self.undo)
        self.redo_button.clicked.connect(self.redo)
        self.clear_button.clicked.connect(self.clear)

    def select_all(self):
        self.text_edit.selectAll()
    def copy(self):
        self.text_edit.copy()
    def paste(self):
        self.text_edit.paste()
    def undo(self):
        self.text_edit.undo()
    def redo(self):
        self.text_edit.redo()
    def clear(self):
        self.text_edit.clear()
    
