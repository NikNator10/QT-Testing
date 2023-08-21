from PySide6.QtWidgets import QWidget, QFontDialog
from PySide6.QtGui import QFont
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Font - Selector")

        self.button.clicked.connect(self.select_font)

    def select_font(self):
        ok,font = QFontDialog.getFont(QFont("Arial", 12), self)
        if ok:
            self.label.setFont(font)
        else:
            print("No font selected")
