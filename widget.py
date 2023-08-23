from PySide6.QtWidgets import QWidget, QFontDialog, QColorDialog
from PySide6.QtGui import QPalette, QFont
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Change your text/background color & font")
        self.label.setAutoFillBackground(True)

        self.text_color_button.clicked.connect(self.set_text_color)
        self.background_color_button.clicked.connect(self.set_background_color)
        self.font_button.clicked.connect(self.set_font)

    def set_text_color(self):
        palette = self.label.palette()
        color = palette.color(QPalette.WindowText)
        chosenColor = QColorDialog.getColor(color, self, "Choose text color")

        if chosenColor.isValid():
            palette.setColor(QPalette.WindowText, chosenColor)
            self.label.setPalette(palette)
        else:
            print("No vaild color selected")
    
    def set_background_color(self):
        palette = self.label.palette()
        color = palette.color(QPalette.Window)
        chosenColor = QColorDialog.getColor(color, self, "Choose background color")

        if chosenColor.isValid():
            palette.setColor(QPalette.Window, chosenColor)
            self.label.setPalette(palette)
        else:
            print("No valid color selected")
    
    def set_font(self):
        ok,font = QFontDialog.getFont(QFont("Arial", 20), self)
        if ok:
            self.label.setFont(font)
        else:
            print("No valid font selected")