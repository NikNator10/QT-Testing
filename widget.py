from PySide6.QtWidgets import QWidget, QInputDialog
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QInputDialog - Demo")
        
        self.get_item_button.clicked.connect(self.get_item)
        self.get_int_button.clicked.connect(self.get_int)
        self.get_double_button.clicked.connect(self.get_double)
        self.get_text_button.clicked.connect(self.get_text)

    def get_item(self):
        items = ["Spring", "Summer", "Autumn", "Winter"]
        item,ok = QInputDialog.getItem(self, "getItem", "Select item:", items)
        if ok:
            print(item)
        else:
            print("No valid input")

    def get_int(self):
        val,ok = QInputDialog.getInt(self, "getInt", "Set your value:", 50, 0 , 100) # 50, 0 ,100 = default value, min value , max value
        if ok:
            print(val)
        else:
            print("No valid input")
        
    def get_double(self):
        val, ok = QInputDialog.getDouble(self, "getDouble", "Value:", 25, 0, 100)
        if ok:
            print(val)
        else:
            print("No valid input")
    

    def get_text(self):
        txt,ok = QInputDialog.getText(self, "getText", "Enter text:")
        if ok and not txt == '':
            print(txt)
        else:
            print("No valid input")