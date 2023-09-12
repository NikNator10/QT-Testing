from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QListWidget, QFileDialog, QMessageBox
from PySide6.QtCore import QDir, QFileInfo

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDir - Demo")

        choose_dir_button = QPushButton("Choose Directory")
        create_dir_button = QPushButton("Create Directory")
        delete_dir_button = QPushButton("Delete Directory")
        dir_exists_button = QPushButton("Does Dir exist?")
        list_folder_conten_button = QPushButton("List folder content")
        dir_file_button = QPushButton("Dir or file?")

        self.line_edit = QLineEdit()
        self.list_widget = QListWidget()

        v_button_layout = QVBoxLayout()
        v_button_layout.addWidget(choose_dir_button)
        v_button_layout.addWidget(create_dir_button)
        v_button_layout.addWidget(delete_dir_button)
        v_button_layout.addWidget(dir_exists_button)
        v_button_layout.addWidget(list_folder_conten_button)
        v_button_layout.addWidget(dir_file_button)

        v_line_list_layout = QVBoxLayout()
        v_line_list_layout.addWidget(self.line_edit)
        v_line_list_layout.addWidget(self.list_widget)

        h_layout = QHBoxLayout()
        h_layout.addLayout(v_line_list_layout)
        h_layout.addLayout(v_button_layout)

        self.setLayout(h_layout)

        choose_dir_button.clicked.connect(self.choose_dir)
        create_dir_button.clicked.connect(self.create_dir)
        delete_dir_button.clicked.connect(self.delete_dir)
        dir_exists_button.clicked.connect(self.dir_exists)
        list_folder_conten_button.clicked.connect(self.list_folder_content)
        dir_file_button.clicked.connect(self.dir_file)

    def choose_dir(self):
        dir_path = QFileDialog.getExistingDirectory(self, "Choose directory")
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
    
    def delete_dir(self):
        dir_path = self.line_edit.text()
        if dir_path == "":
            return
        dir = QDir(dir_path)
        if dir.rmdir(dir_path):
            QMessageBox.information(self, "Directory", "Directory deleted successfully")
        else:
            QMessageBox.information(self, "Directory", "Could not delete directory: Directory does not exist")
        
    def dir_exists(self):
        dir_path = self.line_edit.text()
        if dir_path == "":
            return
        dir = QDir(dir_path)
        if dir.exists():
            QMessageBox.information(self, "Directory", "Directory exists")
        else:
            QMessageBox.information(self, "Directory", "Directory does not exist")
    
    def list_folder_content(self):
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