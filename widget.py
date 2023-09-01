from PySide6.QtWidgets import QWidget, QMessageBox, QFileDialog
from PySide6.QtCore import QFile, QIODevice, QTextStream
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QFile - Demo")

        self.save_file_button.clicked.connect(self.save_file)
        self.open_file_button.clicked.connect(self.open_file)
        self.select_file_button.clicked.connect(self.select_file)
        self.copy_file_button.clicked.connect(self.copy_file)

    def save_file(self):
        file_name,_ = QFileDialog.getSaveFileName(self, "Save File", "untitled", "Text (*.txt);;All Files (*.*)")
        if file_name == '':
            return
        print(f"file name: {file_name}")
        file = QFile(file_name)
        if not file.open(QIODevice.WriteOnly | QIODevice.Text):
            return
        
        out_stream = QTextStream(file)
        out_stream << self.text_edit.toPlainText()
        file.close()

    def open_file(self):
        file_name,_ = QFileDialog.getOpenFileName(self, "Open File", "text", "Text (*.txt);;All Files (*.*)")
        if file_name == '':
            return
        print(f"file name: {file_name}")
        file = QFile(file_name)
        if not file.open(QIODevice.ReadOnly | QIODevice.Text):
            return
        in_stream = QTextStream(file)
        while not in_stream.atEnd():
            line = in_stream.readLine()
            file_content = ''
            file_content += line
        file.close()
        self.text_edit.clear()
        self.text_edit.setText(file_content)

    def select_file(self):
        file_name,_ = QFileDialog.getOpenFileName(self, "Select a file", "untitled", "Text (*.txt);; All Files (*.*)")
        if file_name == '':
            return
        self.source_line_edit.setText(file_name)
    
    def copy_file(self):
        source = self.source_line_edit.text()
        destination = self.destination_line_edit.text()
        if source == '' or destination == '':
            return
        
        file = QFile(source)
        if file.copy(destination):
            QMessageBox.information(self, "File", "File successfully copied")
        else:
            QMessageBox.information(self, "File", "Could not copy file")
    