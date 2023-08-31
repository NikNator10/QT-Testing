from PySide6.QtCore import Qt, QSettings
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget, QColorDialog
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.color_list = [Qt.black, Qt.black, Qt.black, Qt.black, Qt.black, Qt.black]

        self.button_1.clicked.connect(self.button_1_clicked)
        self.button_2.clicked.connect(self.button_2_clicked)
        self.button_3.clicked.connect(self.button_3_clicked)
        self.button_4.clicked.connect(self.button_4_clicked)
        self.button_5.clicked.connect(self.button_5_clicked)
        self.button_6.clicked.connect(self.button_6_clicked)

        self.save_color_button.clicked.connect(self.save_color_button_clicked)
        self.load_color_button.clicked.connect(self.load_color_button_clicked)

    def button_1_clicked(self):
        color = QColorDialog.getColor(self.color_list[0], self, "Choose a background color")
        if color.isValid():
            self.color_list[0] = color
            css = "background-color:" + color.name()
            self.button_1.setStyleSheet(css)
    
    def button_2_clicked(self):
        color = QColorDialog.getColor(self.color_list[1], self, "Choose a background color")
        if color.isValid():
            self.color_list[1] = color
            css = "background-color:" + color.name()
            self.button_2.setStyleSheet(css)

    def button_3_clicked(self):
        color = QColorDialog.getColor(self.color_list[2], self, "Choose a background color")
        if color.isValid():
            self.color_list[2] = color
            css = "background-color:" + color.name()
            self.button_3.setStyleSheet(css)
    
    def button_4_clicked(self):
        color = QColorDialog.getColor(self.color_list[3], self, "Choose a background color")
        if color.isValid():
            self.color_list[3] = color
            css = "background-color:" + color.name()
            self.button_4.setStyleSheet(css)
    
    def button_5_clicked(self):
        color = QColorDialog.getColor(self.color_list[4], self, "Choose a background color")
        if color.isValid():
            self.color_list[4] = color
            css = "background-color:" + color.name()
            self.button_5.setStyleSheet(css)
    
    def button_6_clicked(self):
        color = QColorDialog.getColor(self.color_list[5], self, "Choose a background color")
        if color.isValid():
            self.color_list[5] = color
            css = "background-color:" + color.name()
            self.button_6.setStyleSheet(css)

    def save_color(self, key, color): 
        l_color = QColor(color)
        red = l_color.red() 
        green =l_color.green() 
        blue = l_color.blue() 

        settings = QSettings("Your Company Name", "Your Product Name")
        settings.beginGroup("ButtonColor")
        settings.setValue(key + "r", red)
        settings.setValue(key + "g", green)
        settings.setValue(key + "b", blue)
        settings.endGroup()

    def load_color(self, key):
        settings = QSettings("Your Company Name", "Your Product Name")
        settings.beginGroup("ButtonColor")
        red = settings.value(key + "r")
        green = settings.value(key + "g")
        blue = settings.value(key + "b")
        settings.endGroup()
        return QColor(red, green, blue)

    def set_loaded_color(self,key,index,button): 
        color = self.load_color(key)
        self.color_list[index] = color
        css = "background-color:" + color.name()
        button.setStyleSheet(css)

    def load_color_button_clicked(self):
        self.set_loaded_color("button_1", 0, self.button_1)
        self.set_loaded_color("button_2", 1, self.button_2)
        self.set_loaded_color("button_3", 2, self.button_3)
        self.set_loaded_color("button_4", 3, self.button_4)
        self.set_loaded_color("button_5", 4, self.button_5)
        self.set_loaded_color("button_6", 5, self.button_6)

    def save_color_button_clicked(self):
        self.save_color("button_1", self.color_list[0])
        self.save_color("button_2", self.color_list[1])
        self.save_color("button_3", self.color_list[2])
        self.save_color("button_4", self.color_list[3])
        self.save_color("button_5", self.color_list[4])
        self.save_color("button_6", self.color_list[5])