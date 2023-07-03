from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QSizePolicy, QLabel, QVBoxLayout, QToolBar, QMessageBox, QStatusBar
from PySide6.QtGui import QPixmap

class GridLayout(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("QGridLayout-Testing")

        tool_bar = QToolBar()
        quit_action = tool_bar.addAction("Quit")
        quit_action.triggered.connect(self.quit)
        about_action = tool_bar.addAction("About")
        about_action.triggered.connect(self.about)

        img_label = QLabel()
        img_label.setPixmap(QPixmap("concept.png"))

        button_1 = QPushButton("1")
        button_2 = QPushButton("2")
        button_2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        button_3 = QPushButton("3")
        button_3.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        button_4 = QPushButton("4")
        button_5 = QPushButton("5")
        button_6 = QPushButton("6")
        button_7 = QPushButton("7")
        button_8 = QPushButton("8")
        button_9 = QPushButton("9")
        button_9.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        button_10 = QPushButton("10")
        button_11 = QPushButton("11")
        button_12 = QPushButton("12")

        status_bar = QStatusBar()
        status_bar.showMessage("Program initialized")

        g_layout = QGridLayout()
        g_layout.addWidget(button_1,0,0,1,2)
        g_layout.addWidget(button_2,0,2,2,1)
        g_layout.addWidget(button_3,1,0,2,1)
        g_layout.addWidget(button_4,1,1)
        g_layout.addWidget(button_5,2,1,1,2)
        g_layout.addWidget(button_6,3,0,1,3)
        g_layout.addWidget(button_7,4,0,1,2)
        g_layout.addWidget(button_8,4,2)
        g_layout.addWidget(button_9,5,0,2,1)
        g_layout.addWidget(button_10,5,1,1,2)
        g_layout.addWidget(button_11,6,1)
        g_layout.addWidget(button_12,6,2)

        v_layout = QVBoxLayout()
        v_layout.addWidget(tool_bar)
        v_layout.addWidget(img_label)
        v_layout.addLayout(g_layout)
        v_layout.addWidget(status_bar)
        self.setLayout(v_layout)
   
    def quit(self,app):
        self.app.quit()

    def about(self):
        QMessageBox.about(self,"About", "QGridLayout-Testing")