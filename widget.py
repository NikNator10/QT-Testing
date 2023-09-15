from PySide6.QtWidgets import QWidget
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from PySide6.QtCore import QByteArray, QUrl
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Netowrking in Qt")

        self.network_access_manager = QNetworkAccessManager(self)
        self.data = QByteArray()
        self.request = QNetworkRequest()

        self.request.setUrl(QUrl("https://google.com"))

        self.net_reply = self.network_access_manager.get(self.request)
        self.net_reply.readyRead.connect(self.data_ready)
        self.net_reply.finished.connect(self.finished)

    def data_ready(self):
        print("Data recieved")
        self.data.append(self.net_reply.readAll())
    
    def finished(self):
        print("Data read finished")
        if self.net_reply.error() is not QNetworkReply.NoError:
            print("Some error occurred")
        else:
            self.textEdit.setText(str(self.data))