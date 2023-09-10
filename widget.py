from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import QDir, QFileInfo
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QDir - Demo")

        self.choose_dir_button.clicked.connect(self.choose_dir)
        self.create_dir_button.clicked.connect(self.create_dir)
        self.delete_dir_button.clicked.connect(self.delete_dir)
        self.dir_exists_button.clicked.connect(self.dir_exists)
        self.folder_content_button.clicked.connect(self.folder_content)
        self.dir_file_button.clicked.connect(self.dir_file)
        
    def choose_dir(self):
        dir_path = QFileDialog.getExistingDirectory(self, "Choose Directory")
        if dir_path == "":
            return
        self.line_edit.setText(dir_path)

    def create_dir(self):
        dir_path = self.line_edit.text()
        if dir_path == "":
            return
        dir = QDir(dir_path)
        if dir.mkdir(dir_path):
            QMessageBox.information(self, "Directory", "Created directory successfully")
        else:
            QMessageBox.information(self, "Directory", "Could not create directory: Directory already exists")

    def delete_dir(self):
        dir_path = self.line_edit.text()
        if dir_path == "":
            return
        dir = QDir(dir_path)
        if dir.rmdir(dir_path):
            QMessageBox.information(self, "Directory", "Removed directory successfully")
        else:
            QMessageBox.information(self, "Directory", "Could not remove directory: Directory doesn't exist")

    def dir_exists(self):
        dir_path = self.line_edit.text()
        if dir_path == "":
            return
        dir = QDir(dir_path)
        if dir.exists():
            QMessageBox.information(self, "Directory", "Directory exists")
        else:
            QMessageBox.information(self, "Directory", "Directory doesn't exist")

    def folder_content(self):
        dir_path = self.line_edit.text()
        if dir_path == "":
            return
        dir = QDir(dir_path)
        file_list = dir.entryInfoList()
        self.list_widget.clear()
        for i in range(len(file_list)):
            file_info = QFileInfo(file_list[i])
            self.list_widget.addItem(file_info.absoluteFilePath())

    def dir_file(self):
        file_info = QFileInfo(self.list_widget.currentItem().text())
        if file_info.isFile():
            QMessageBox.information(self, "Directory", "The selected object is a file")
        else:
            QMessageBox.information(self, "Directory", "The selected object is a directory")