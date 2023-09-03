from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import QFile, QIODevice, QTextStream
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Save & Open Files")

        self.open_file_button.clicked.connect(self.open_file)
        self.save_file_button.clicked.connect(self.save_file)
        
    def open_file(self):
        # Fixed bug from commit 987c358: file_content = '' should not be in while not in_stream.atEnd():
        file_content = ''

        file_name,_ = QFileDialog.getOpenFileName(self, "Open File", "", "Text (*.txt);;All Files (*.*)")
        if file_name == '':
            return
        print(f"file name: {file_name}")
        file = QFile(file_name)
        if not file.open(QIODevice.ReadOnly | QIODevice.Text):
            return
        in_stream = QTextStream(file)
        while not in_stream.atEnd():
            line = in_stream.readLine()
            # Another fixed bug from previous commits 987c358 and 03ca6eb
            file_content += '\n'
            
            file_content += line
        file.close()
        self.text_edit.clear()
        self.text_edit.setText(file_content)

    def save_file(self):
        file_name,_ = QFileDialog.getSaveFileName(self, "Save File", "", "Text (*.txt);; All Files (*.*)")
        if file_name == '':
            return
        file = QFile(file_name)
        if not file.open(QIODevice.WriteOnly | QIODevice.Text):
            return
        out_stream = QTextStream(file)
        out_stream << self.text_edit.toPlainText()
        file.close()