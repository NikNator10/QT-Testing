from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMenuBar, QToolBar, QMessageBox

class Widget(QWidget):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("Data-Form") 
        self.app = app

        # Creates a menubar with a quit action and a shortcut to use it
        menu_bar = QMenuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit)
        quit_action.setShortcut("Ctrl+q")
        
        # Creates a toolbar and adds an action to it
        tool_bar = QToolBar()
        tool_bar.addAction(quit_action)
        
        # Creates the labels and line edits for the form
        label_fname = QLabel("First Name: ")
        self.line_fname = QLineEdit()

        label_lname = QLabel("Last Name: ")
        self.line_lname = QLineEdit()

        label_address = QLabel("Address: ")
        self.line_address = QLineEdit()

        send_button = QPushButton("Send")
        send_button.pressed.connect(self.send_data)
        self.label_status = QLabel("Status: ")

        # Sets the horizontal layout for the labels and line edits
        h_layout_fname = QHBoxLayout()
        h_layout_fname.addWidget(label_fname)
        h_layout_fname.addWidget(self.line_fname)
        
        h_layout_lname = QHBoxLayout()
        h_layout_lname.addWidget(label_lname)
        h_layout_lname.addWidget(self.line_lname)

        h_layout_address = QHBoxLayout()
        h_layout_address.addWidget(label_address)
        h_layout_address.addWidget(self.line_address)

        # Creates one big vertical layout
        v_layout = QVBoxLayout()
        v_layout.addWidget(menu_bar)
        v_layout.addWidget(tool_bar)
        v_layout.addLayout(h_layout_fname)
        v_layout.addLayout(h_layout_lname)
        v_layout.addLayout(h_layout_address)
        v_layout.addWidget(send_button)
        v_layout.addWidget(self.label_status)
        self.setLayout(v_layout)

    def quit(self):
      self.app.quit()

    # Sends the data to the console
    def send_data(self):
       QMessageBox.information(self, "Information", "Data received, look in your console", QMessageBox.Ok)
       print("First Name: ", self.line_fname.text())
       print("Last Name: ", self.line_lname.text())
       print("Address: ", self.line_address.text())
       self.label_status.setText("Status: Data collected")