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
        self.remove_dir_button.clicked.connect(self.remove_dir)
        self.folder_content_button.clicked.connect(self.folder_content)
        self.dir_exists_button.clicked.connect(self.dir_exists)
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
            QMessageBox.information(self, "Directory", "Directory created successfully")
        else:
            QMessageBox.information(self, "Directory", "Could not create directory: Directory already exists")

    def remove_dir(self):
        dir_path = self.line_edit.text()
        if dir_path == "":
            return
        dir = QDir(dir_path)
        if dir.rmdir(dir_path):
            QMessageBox.information(self, "Directory", "Directory removed successfully")
        else:
            QMessageBox.information(self, "Directory", "Could not remove directory: Directory does not exist")
    
    def dir_exists(self):
        dir_path = self.line_edit.text()
        if dir_path == "":
            return
        dir = QDir(dir_path)
        if dir.exists():
            QMessageBox.information(self, "Directory", "Directory exists")
        else:
            QMessageBox.information(self, "Directory", "Directory does not exist")

    def folder_content(self):
        dir_path = self.line_edit.text()
        if dir_path == "":
            return
        dir = QDir(dir_path)
        file_list = dir.entryInfoList()
        for i in range(len(file_list)):
            file_info = QFileInfo(file_list[i])
            self.list_widget.addItem(file_info.absoluteFilePath())
    
    def dir_file(self):
        file_info = QFileInfo(self.list_widget.currentItem().text())
        if file_info.isFile():
            QMessageBox.information(self, "Directory", "The selected object is a file")
        else:
            QMessageBox.information(self, "Directory", "The selected object is a directory")
        