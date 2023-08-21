from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFileDialog - Demo")

        self.resize(300,100)

        get_existing_dir_button = QPushButton("getExistingDirectory")
        get_open_file_name = QPushButton("getOpenFileName")
        get_open_file_names = QPushButton("getOpenFileNames")
        get_save_file_name = QPushButton("getSaveFileName")

        get_existing_dir_button.clicked.connect(self.get_dir)
        get_open_file_name.clicked.connect(self.get_open_file_name)
        get_open_file_names.clicked.connect(self.get_open_file_names)
        get_save_file_name.clicked.connect(self.get_save_file_name)

        v_layout = QVBoxLayout()
        v_layout.addWidget(get_existing_dir_button)
        v_layout.addWidget(get_open_file_name)
        v_layout.addWidget(get_open_file_names)
        v_layout.addWidget(get_save_file_name)
        self.setLayout(v_layout)

    def get_dir(self):
        dir = QFileDialog.getExistingDirectory(self, "Open Directory", "", QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        print(dir)
    def get_open_file_name(self):
        file_name,_ = QFileDialog.getOpenFileName(self, "Open File", "/home", "Images (*.png *.jpg);;All Files (*.*)")
        print(file_name)
    def get_open_file_names(self):
        file_names,_ = QFileDialog.getOpenFileNames(self, "Open Files", "/home", "Images (*.png *.jpg);;All Files (*.*)")
        for f in file_names:
            print(f)
    def get_save_file_name(self):
        file_name,_ = QFileDialog.getSaveFileName(self, "Save File", "/home", "Images (*.png *.jpg);;All Files (*.*)")
        print(file_name)