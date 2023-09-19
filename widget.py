from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QInputDialog, QFileDialog, QPushButton
from PySide6.QtCore import QUrl, QByteArray, QFile, QIODevice, QTextStream
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic Networking in Qt")

        self.text_edit = QTextEdit()
        save_to_file_button = QPushButton("Save to file")
        save_to_file_button.clicked.connect(self.save_file)
        
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.text_edit)
        v_layout.addWidget(save_to_file_button)
        self.setLayout(v_layout)

        self.manager = QNetworkAccessManager(self)
        self.data_buffer = QByteArray()
        self.request = QNetworkRequest()
        
        url,ok = QInputDialog.getText(self, "URL", "Enter URL:")
        if ok and not url == "":
            self.request.setUrl(QUrl(url))

        self.net_reply = self.manager.get(self.request)
        self.net_reply.readyRead.connect(self.data_read_ready)
        self.net_reply.finished.connect(self.data_read_finished)

    def data_read_ready(self):
        print("Data recieved!")
        self.data_buffer.append(self.net_reply.readAll())

    def data_read_finished(self):
        print("Data read finished")
        if self.net_reply.error() is not QNetworkReply.NoError:
            print("Some error occurred")
        else:
            self.text_edit.setText(str(self.data_buffer))
    
    def save_file(self):
        file_name,_ = QFileDialog.getSaveFileName(self, "Save File", "", "Text (*.txt)")
        if file_name == "":
            return
        file = QFile(file_name)
        if not file.open(QIODevice.WriteOnly | QIODevice.Text):
            return
        out_stream = QTextStream(file)
        out_stream << self.text_edit.toPlainText()