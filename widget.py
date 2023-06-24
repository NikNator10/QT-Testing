from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QHBoxLayout,QSizePolicy, QVBoxLayout
from PySide6.QtGui import QPixmap

class Edit(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Size Policy, stretches and pixmap")

        label = QLabel("Enter Text: ")
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        line_edit = QLineEdit()
        line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        button_1 = QPushButton("One")
        button_1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        button_2 = QPushButton("Two")
        button_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        button_3 = QPushButton("Three")
        button_3.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        img = QLabel()
        img.setPixmap(QPixmap("images/pymeme.jpg"))

        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(label)
        h_layout_1.addWidget(line_edit)

        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(button_1)
        h_layout_2.addWidget(button_2, 2)
        h_layout_2.addWidget(button_3)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout_1)
        v_layout.addLayout(h_layout_2)
        v_layout.addWidget(img)
        self.setLayout(v_layout)