from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QToolBar
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Windows 12 Setup")
        self.setWindowIcon(QIcon("setup.png"))

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.setShortcut("Ctrl+q")
        quit_action.triggered.connect(self.quit_trigger)
        
        tool_bar = QToolBar()
        tool_bar.setIconSize(QSize(16,16))
        self.addToolBar(tool_bar)
        tool_bar.addAction(quit_action)

    def quit_trigger(self):
        self.app.quit()