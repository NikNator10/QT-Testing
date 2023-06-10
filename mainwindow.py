from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMenuBar, QToolBar
import sys

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Window")
        window = QMainWindow()
        button = QPushButton("Button")
        self.setCentralWidget(button)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        about_menu = menu_bar.addMenu("About")
        
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_trigger)
        quit_action.setShortcut("Ctrl+q")

        tool_bar = QToolBar()
        tool_bar.setIconSize(QSize(16,16))
        self.addToolBar(tool_bar)
        tool_bar.addAction(quit_action)
        tool_bar.addAction(quit_action)
        
        action1 = QAction(QIcon("start.png"), "Quit", self)
        tool_bar.addAction(action1)
        action1.triggered.connect(self.quit_trigger)

    def quit_trigger(self):
        self.app.quit()