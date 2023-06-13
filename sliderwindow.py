from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QSlider, QToolBar

def slider_change(data):
    print("Slider changed to:", data)

class SliderMainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Slider")
        slider = QSlider(Qt.Horizontal)
        self.setCentralWidget(slider)
        slider.setMinimum(1)
        slider.setMaximum(1000)
        slider.setValue(500)
        slider.valueChanged.connect(slider_change)
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.setShortcut("Ctrl+q")
        quit_action.triggered.connect(self.quit_trigger)
        tool_bar = QToolBar()
        self.addToolBar(tool_bar)
        tool_bar.addAction(quit_action)

    def quit_trigger(self):
        self.app.quit()