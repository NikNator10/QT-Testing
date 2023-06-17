from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QMenuBar, QToolBar, QMessageBox
from PySide6.QtCore import Qt

class Widget(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.setWindowTitle("Widget")

        # Create buttons
        button1 = QPushButton("Critical MessageBox")
        button2 = QPushButton("Add new Button")
        button2.setCheckable(True)
        button3 = QPushButton("About")

        button1.clicked.connect(self.crit_msgbox)
        button2.clicked.connect(self.new_button)
        button3.clicked.connect(self.about_msgbox)

        # Adds a MenuBar and actions
        menu_bar = QMenuBar() # Wie bringe ich die MenuBar und ToolBar nach oben?
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        about_msgbox = file_menu.addAction("About")

        # Adds a ToolBar with separators and 2 actions
        tool_bar = QToolBar()
        tool_bar.addAction(quit_action)
        tool_bar.addSeparator()
        tool_bar.addAction(about_msgbox)

        # Link to actions
        quit_action.triggered.connect(self.quit_action)
        about_msgbox.triggered.connect(self.about_msgbox)

        # Select vertical or horizontal layout (QHBoxLayout or QVBoxLayout)
        layout = QHBoxLayout()

        # Adds the buttons to the layout
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        # Adds the MenuBar and ToolBar to the layout
        layout.addWidget(menu_bar)
        layout.addWidget(tool_bar)
        # Applies the set layout
        self.setLayout(layout)

    def quit_action(self, app):
        self.app.quit()

    def crit_msgbox(self):
        ret = QMessageBox.critical(self, "Error", "This is an error", QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("Ok")
        else:
            print("Cancel")

    def new_button(self):
        if self.sender().isChecked():
            button4 = QPushButton("Newest Button")
            self.layout().addWidget(button4)


    def about_msgbox(self):
        ret = QMessageBox.about(self, "About", "About site")