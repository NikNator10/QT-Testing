from PySide6.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout, QSlider, QWidget, QMenuBar, QToolBar
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QAction

class MainWindow(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("MainWindow")
        self.setWindowIcon(QIcon("windowicon.png"))
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Add Button")
        button3.setCheckable(True)
        button3.clicked.connect(self.button_add)

        slider = QSlider()
        slider.setMinimum(1)
        slider.setMaximum(100)
        slider.setValue(42)
        slider.valueChanged.connect(self.slider_value)
        self.layout_h = QHBoxLayout()

        menu_bar = QMenuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.setShortcut("Ctrl+q")
        quit_action.triggered.connect(self.quit_action)

        action = QAction("Quit", self)
        action.setToolTip("Quit")
        action.setIcon(QIcon("exit.png"))
        action.triggered.connect(self.quit_action)

        tool_bar = QToolBar()
        tool_bar.addAction(action)

        self.layout_h.addWidget(button1)
        self.layout_h.addWidget(button2)
        self.layout_h.addWidget(button3)
        self.layout_h.addWidget(slider)
        self.layout_h.addWidget(menu_bar)
        self.layout_h.addWidget(tool_bar)

        self.setLayout(self.layout_h)
        
    def button_add(self):
            if self.sender().isChecked():
                button5 = QPushButton("New Button")
                self.layout().addWidget(button5)

    def slider_value(self, data):
         print("Slider changed to", data)
         if data == 1:
             print("Min reached")
         elif data == 100:
            print("Max reached")
    
    def quit_action(self, app):
        self.app.quit()
        


""" Wieso geht das nicht?
        self.current_layout = "horizontal"
        button4 = QPushButton("Change Layout")

        
        self.layout_v = QVBoxLayout()
        self.layout_v.addWidget(button1)
        self.layout_v.addWidget(button2)
        self.layout_v.addWidget(button3)
        self.layout_v.addWidget(button4)
        self.layout_v.addWidget(slider)
        
        button4.setCheckable(True)
        button4.clicked.connect(self.layout_change)

    def layout_change(self):
        
        ( while self.sender().isChecked: ) bringt das Programm zum Absturz - selbst wenn man time einbaut
        if self.current_layout == "horizontal":
                self.setLayout(self.layout_v)
                self.current_layout = "vertical")
        else:
                self.setLayout(self.layout_h)
                self.current_layout = "horizontal"
"""