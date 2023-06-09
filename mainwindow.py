from PySide6.QtCore import Qt,QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMenuBar, QPushButton, QToolBar
from PySide6.QtGui import QAction
import sys

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Fenstername")
        button = QPushButton("Button")
        button.clicked.connect(self.button_state) #Wie baue ich ein setCheckable(True) ein?
 
        self.setCentralWidget(button)

        menu_bar =  self.menuBar()
        file_menu = menu_bar.addMenu("File")
        new_page_menu = file_menu.addAction("New")
        open_page_menu = file_menu.addAction("Open")
        save_actoin = file_menu.addAction("Save")

        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_trigger)
        quit_action.setShortcut('Ctrl+Q')

        toolbar = QToolBar()
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)
        toolbar.addAction(quit_action)

        debug_action = QAction("Debug", self)
        debug_action.triggered.connect(self.debug_trigger)
        toolbar.addAction(debug_action)

    def quit_trigger(self):
        self.app.quit()

    def debug_trigger(self):
        print("Debugging works")
    
    def button_state(data):
        print("Button pressed")
