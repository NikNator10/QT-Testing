from PySide6.QtWidgets import QDialog, QPushButton, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout

class Infodialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enter Data")

        label = QLabel("Name: ")
        self.line_edit = QLineEdit()

        ok_button = QPushButton("Ok")
        ok_button.clicked.connect(self.accept_input)
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)

        h_enter_name_layout = QHBoxLayout()
        h_enter_name_layout.addWidget(label)
        h_enter_name_layout.addWidget(self.line_edit)

        h_button_layout = QHBoxLayout()
        h_button_layout.addWidget(ok_button)
        h_button_layout.addWidget(cancel_button)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_enter_name_layout)
        v_layout.addLayout(h_button_layout)
        self.setLayout(v_layout)
    
    def accept_input(self):
        if not self.line_edit.text() == '':
            self.name = self.line_edit.text()
            print("Dialog accepted")
            self.accept()    