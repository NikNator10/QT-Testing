from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import QFile
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Copy files")

        self.choose_file_button.clicked.connect(self.choose_file)
        self.copy_button.clicked.connect(self.copy_file)

    def choose_file(self):
        file_name,_ = QFileDialog.getOpenFileName(self, "Choose File", "", "Text-File (*.txt);;Images (*.png *.jpg);;All Files (*.*)")
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