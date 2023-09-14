from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QByteArray, QUrl
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Basic Networking with QT")

        self.manager = QNetworkAccessManager(self)
        self.data_buffer = QByteArray()
        self.request = QNetworkRequest()

        self.request.setUrl(QUrl("https://github.com"))

        self.net_reply = self.manager.get(self.request)
        self.net_reply.readyRead.connect(self.data_ready_to_read)
        self.net_reply.finished.connect(self.data_read_finished)
    
    def data_ready_to_read(self):
        print("Data available")
        self.data_buffer.append(self.net_reply.readAll())
    
    def data_read_finished(self):
        print("Data read finished")
        if self.net_reply.error() is not QNetworkReply.NoError:
            print("Some error occurred")
        else:
            self.textEdit.setText(str(self.data_buffer))