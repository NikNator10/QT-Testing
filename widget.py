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
        self.dir_exists_button.clicked.connect(self.dir_exists)
        self.dir_or_file_button.clicked.connect(self.dir_or_file)
        self.folder_content_button.clicked.connect(self.folder_content)  

    def choose_dir(self):
        dir_path = QFileDialog.getExistingDirectory(self, "Choose directory")
        if dir_path == "":
            return
        print(f"Dir path: {dir_path}")
        self.dir_path_line_edit.setText(dir_path)

    def create_dir(self):
        dir_path = self.dir_path_line_edit.text()
        if dir_path == "":
            return
        dir = QDir(dir_path)
        if not dir.exists():
            if dir.mkdir(dir_path):
                QMessageBox.information(self, "Success", "Directory created successfully")     
        else:
            QMessageBox.information(self, "Error", "Directory already exists")

    def dir_exists(self):
        dir_path = self.dir_path_line_edit.text()
        if dir_path == "":
            return
        dir = QDir(dir_path)
        if dir.exists():
            QMessageBox.information(self, "Directory", "Directory exists")
        else:
            QMessageBox.information(self, "Directory", "This directory doesn't exist")

    def folder_content(self):
        dir_path = self.dir_path_line_edit.text()
        if dir_path == "":
            return
        dir = QDir(dir_path)
        file_list = dir.entryInfoList()
        for i in range(len(file_list)):
            file_info  = QFileInfo(file_list[i])
            self.list_widget.addItem(file_info.absoluteFilePath())

    def dir_or_file(self):
        file_info = QFileInfo(self.list_widget.currentItem().text())
        if file_info.isFile():
            QMessageBox.information(self, "Info", "You selected a file")
        else:
            QMessageBox.information(self, "Info", "You selected a directory")