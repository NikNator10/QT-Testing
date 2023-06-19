from PySide6.QtWidgets import QWidget, QMenuBar, QToolBar, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox

class DataForm(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Data Collector")

        menu_bar = QMenuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.setShortcut("Ctrl+q")
        about_action = file_menu.addAction("About")
        about_action.setShortcut("Ctrl+u")

        tool_bar = QToolBar()
        tool_bar.addAction(quit_action)
        tool_bar.addAction(about_action)

        quit_action.triggered.connect(self.quit_action)
        about_action.triggered.connect(self.about_action)

        label_fname = QLabel("First Name: ")
        self.line_fname = QLineEdit()

        label_lname = QLabel("Last Name: ")
        self.line_lname = QLineEdit()

        label_address = QLabel("Address: ")
        self.line_address = QLineEdit()
        self.line_address.returnPressed.connect(self.send_input)


        send_button = QPushButton("Send")
        send_button.clicked.connect(self.send_input)


        self.label_status = QLabel("Status: ")

        v_layout = QVBoxLayout()
        v_layout.addWidget(menu_bar)
        v_layout.addWidget(tool_bar)
        v_layout.addWidget(label_fname)
        v_layout.addWidget(self.line_fname)
        v_layout.addWidget(label_lname)
        v_layout.addWidget(self.line_lname)
        v_layout.addWidget(label_address)
        v_layout.addWidget(self.line_address)
        v_layout.addWidget(send_button)
        v_layout.addWidget(self.label_status)

        self.setLayout(v_layout)





    def send_input(self):
        print("Data collected:")
        print("First Name: ", self.line_fname.text())
        print("Last Name: ", self.line_lname.text())
        print("Address: ", self.line_address.text())
        self.label_status.setText("Status:\nData submitted!")

    def quit_action(self, app):
        self.app.quit()

    def about_action(self):
        QMessageBox.about(self, "About", "This is a data collector")

