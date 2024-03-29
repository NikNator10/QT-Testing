from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QFileDialog
from PySide6.QtCore import QFile, QTextStream, QIODevice

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Save & Open Text-files")

        save_file_button = QPushButton("Save File")
        save_file_button.clicked.connect(self.save_file)
        open_file_button = QPushButton("Open File")
        open_file_button.clicked.connect(self.open_file)
        self.text_edit = QTextEdit()

        v_button_lyaout = QVBoxLayout()
        v_button_lyaout.addWidget(save_file_button)
        v_button_lyaout.addWidget(open_file_button)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.text_edit)
        h_layout.addLayout(v_button_lyaout)
        self.setLayout(h_layout)

    def save_file(self):
        file_name,_ = QFileDialog.getSaveFileName(self, "Save File", "", "Text-File (*.txt);;All Files(*.*)")
        if file_name == "":
            return
        file = QFile(file_name)
        if not file.open(QIODevice.WriteOnly | QIODevice.Text):
            return
        out_stream = QTextStream(file)
        out_stream << self.text_edit.toPlainText()

    def open_file(self):
        file_content = ""
        file_name,_ = QFileDialog.getOpenFileName(self, "Opem File", "", "Text-File (*.txt);;All Files (*.*)")
        if file_name == "":
            return
        file = QFile(file_name)
        if not file.open(QIODevice.ReadOnly | QIODevice.Text):
            return
        in_stream = QTextStream(file)
        while not in_stream.atEnd():
            line = in_stream.readLine()
            file_content += line
            file_content += "\n"
        self.text_edit.clear()
        self.text_edit.setText(file_content)
        