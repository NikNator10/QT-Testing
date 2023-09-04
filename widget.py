from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QLineEdit, QSizePolicy, QMessageBox
from PySide6.QtCore import QFile, QTextStream, QIODevice

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Copy file to another Path")
        self.resize(300,100)
        choose_file_button = QPushButton("Choose File")
        choose_file_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        copy_file_button = QPushButton("Copy File")
        copy_file_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)


        self.src_line_edit = QLineEdit()
        self.src_line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.dst_line_edit = QLineEdit()
        self.dst_line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        h_src_layout = QHBoxLayout()
        h_src_layout.addWidget(self.src_line_edit)
        h_src_layout.addWidget(choose_file_button)

        h_dst_layout = QHBoxLayout()
        h_dst_layout.addWidget(self.dst_line_edit)
        h_dst_layout.addWidget(copy_file_button)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_src_layout)
        v_layout.addLayout(h_dst_layout)
        self.setLayout(v_layout)

        choose_file_button.clicked.connect(self.choose_file)
        copy_file_button.clicked.connect(self.copy_file)

    def choose_file(self):
        file_name,_ = QFileDialog.getOpenFileName(self, "Select a file", "", "Text-File (*.txt);;Images (*.png *.jpg);;All Files (*.*)")
        if file_name == '':
            return
        self.src_line_edit.setText(file_name)
        
    def copy_file(self):
        src = self.src_line_edit.text()
        dst = self.dst_line_edit.text()
        if src == '' or dst == '':
            return
        file = QFile(src)
        if file.copy(dst):
            QMessageBox.information(self, "Success", "File copied successfully")
        else:
            QMessageBox.information(self, "Error", "Could not copy file")