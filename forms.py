from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QLabel, QMenuBar, QToolBar, QMessageBox
from PySide6.QtCore import Qt
class DataForm(QWidget):
    def __init__(self, app):
        super().__init__()

        self.app = app
        self.setWindowTitle("DataForm")

        # Creating a MenuBar
        menu_bar = QMenuBar()
        file_menu = menu_bar.addMenu("File")
        about_action = file_menu.addAction("About")
        about_action.triggered.connect(self.about_msgbox)
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_action)

        # Creating a ToolBar
        tool_bar = QToolBar()
        tool_bar.addAction(quit_action)
        tool_bar.addSeparator()

        # Creates Labels, LineEdits and Silder 
        label_fname = QLabel("First Name: ")
        self.line_edit_fname = QLineEdit()
        
        label_lname = QLabel("Last Name: ")
        self.line_edit_lname = QLineEdit()

        label_address = QLabel("Address: ")
        self.line_edit_address = QLineEdit()

        send_button = QPushButton("Send")
        send_button.released.connect(self.data_input)

        self.data_status = QLabel("Waiting for Data...")

        # Adds Lables and LineEdits to horizontal layouts
        h_layout_menubar = QHBoxLayout()
        h_layout_menubar.addWidget(menu_bar)


        h_layout_fname = QHBoxLayout()
        h_layout_fname.addWidget(label_fname)
        h_layout_fname.addWidget(self.line_edit_fname)

        h_layout_lname = QHBoxLayout()
        h_layout_lname.addWidget(label_lname)
        h_layout_lname.addWidget(self.line_edit_lname)

        h_layout_address = QHBoxLayout()
        h_layout_address.addWidget(label_address)
        h_layout_address.addWidget(self.line_edit_address)

        # Combines horizontal layouts and buttons to a big vertical layout
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout_menubar)
        v_layout.addWidget(tool_bar)
        v_layout.addLayout(h_layout_fname)
        v_layout.addLayout(h_layout_lname)
        v_layout.addLayout(h_layout_address)
        v_layout.addWidget(send_button)
        v_layout.addWidget(self.data_status)

        self.setLayout(v_layout)
    

    def data_input(self):
        QMessageBox.information(self, "Data", "Data sent!", QMessageBox.Ok)
        print("Data collected successfully!")
        print("First Name: ", self.line_edit_fname.text())
        print("Last Name: ", self.line_edit_lname.text())
        print("Address:", self.line_edit_address.text())
        self.data_status.setText("Data received!")

    def quit_action(self, app):
        self.app.quit()
    
    def about_msgbox(self):
        QMessageBox.about(self,"About", "This is a little data collector" )