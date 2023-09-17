from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit
from PySide6.QtCore import QUrl, QByteArray
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic Networking in Qt")

        self.text_edit = QTextEdit()
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.text_edit)
        self.setLayout(v_layout)

        self.manager = QNetworkAccessManager(self)
        self.data_buffer = QByteArray()
        self.request = QNetworkRequest()

        self.request.setUrl(QUrl("https://github.com"))

        self.net_reply = self.manager.get(self.request)
        self.net_reply.readyRead.connect(self.data_ready_read)
        self.net_reply.finished.connect(self.data_load_finished)

    def data_ready_read(self):
        print("Data recieved")
        self.data_buffer.append(self.net_reply.readAll())

    def data_load_finished(self):
        print("Data load finished")
        if self.net_reply.error() is not QNetworkReply.NoError:
            print("Some error occured")
        else:
            self.text_edit.setText(str(self.data_buffer))