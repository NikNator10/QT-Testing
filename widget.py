from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from ui_widget import Ui_Widget

# Used for resource management
import resource_rc

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.spin_box.setValue(50)
        self.minus_button.clicked.connect(self.minus)
        self.plus_button.clicked.connect(self.plus)

        self.minus_button.setIcon(QIcon(":/images/minus.png"))
        self.plus_button.setIcon(QIcon(":/images/plus.png"))

    def minus(self):
        value = self.spin_box.value()
        self.spin_box.setValue(value -1)
    def plus(self):
        value = self.spin_box.value()
        self.spin_box.setValue(value + 1)