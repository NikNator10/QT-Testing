from PySide6.QtWidgets import QWidget, QFileDialog
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QFileDialog - Demo")

        self.get_existing_directory_button.clicked.connect(self.get_dir)
        self.get_open_file_name.clicked.connect(self.get_file)
        self.get_open_file_names.clicked.connect(self.get_files)
        self.get_save_file_name_button.clicked.connect(self.get_save)

    def get_dir(self):
        dir = QFileDialog.getExistingDirectory(self, "Open Directory", "/home", QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        print(dir)
    
    def get_file(self):
        file_name,_ = QFileDialog.getOpenFileName(self, "Open File", "/home", "Images (*.png *.jpg);;All Files (*.*)")
        print(file_name)
    
    def get_files(self):
        file_names,_ = QFileDialog.getOpenFileNames(self, "Open Files", "/home", "Images (*.png *.jpg);;All Files (*.*)")
        for f in file_names:
            print(f)

    def get_save(self):
        file_name,_ = QFileDialog.getSaveFileName(self, "Save File", "untitled.png", "Images (*.png *.jpg);;All Files (*.*)")
        print(file_name)
