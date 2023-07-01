from PySide6.QtWidgets import QWidget, QLineEdit, QLabel, QPushButton, QSizePolicy, QHBoxLayout, QVBoxLayout
from PySide6.QtGui import QPixmap

class Img(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SizePolicy/stretches + Pixmap")

        label = QLabel("Label")
        line_edit = QLineEdit()
        line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


        button_1 = QPushButton("Button 1")
        button_2 = QPushButton("Button 2")
        button_3 = QPushButton("Button 3")

        img_label = QLabel()
        img_label.setPixmap(QPixmap("img/pymeme.jpg"))

        h_label_layout = QHBoxLayout()
        h_label_layout.addWidget(label)
        h_label_layout.addWidget(line_edit)

        h_button_layout = QHBoxLayout()
        h_button_layout.addWidget(button_1)
        h_button_layout.addWidget(button_2,2)
        h_button_layout.addWidget(button_3)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_label_layout)
        v_layout.addLayout(h_button_layout)
        v_layout.addWidget(img_label)
        self.setLayout(v_layout)