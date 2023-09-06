from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QFileDialog, QMessageBox
from PySide6.QtCore import QFile

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Select & Copy files")
        self.resize(400,100)

        self.src_line_edit = QLineEdit()
        self.dst_line_edit = QLineEdit()

        select_file_button = QPushButton("Select Button")
        copy_file_button = QPushButton("Copy File")

        h_src_layout = QHBoxLayout()
        h_src_layout.addWidget(self.src_line_edit)
        h_src_layout.addWidget(select_file_button)

        h_dst_layout = QHBoxLayout()
        h_dst_layout.addWidget(self.dst_line_edit)
        h_dst_layout.addWidget(copy_file_button)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_src_layout)
        v_layout.addLayout(h_dst_layout)
        self.setLayout(v_layout)

        select_file_button.clicked.connect(self.select_file)
        copy_file_button.clicked.connect(self.copy_file)

    def select_file(self):
        file_name,_ = QFileDialog.getOpenFileName(self, "Choose a file", "", "Text-File (*.txt);;All Files (*.*)")
        if file_name == "":
            return
        self.src_line_edit.setText(file_name)

    def copy_file(self):
        src = self.src_line_edit.text()
        dst = self.dst_line_edit.text()
        if src == "" or dst == "":
            return
        file = QFile(src)
        if file.copy(dst):
            QMessageBox.information(self, "Success", "File copied successfully")
        else:
            QMessageBox.information(self, "Error", "Could not copy file")