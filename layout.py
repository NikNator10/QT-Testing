from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap

class GridLayout(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GridLayout")

        concept_label = QLabel()
        concept_label.setPixmap(QPixmap("concept.png"))

        button_1 = QPushButton("One")
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")
        button_3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button_4 = QPushButton("Four")
        button_4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        button_5 = QPushButton("Five")
        button_6 = QPushButton("Six")
        button_7 = QPushButton("Seven")
        button_7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button_8 = QPushButton("Eight")
        button_8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button_9 = QPushButton("Nine")

        grid_layout = QGridLayout()
        grid_layout.addWidget(button_1,0,0)
        grid_layout.addWidget(button_2,0,1)
        grid_layout.addWidget(button_3,0,2,2,1)
        grid_layout.addWidget(button_4,1,0,1,2)
        grid_layout.addWidget(button_5,2,0,1,3)
        grid_layout.addWidget(button_6,3,0)
        grid_layout.addWidget(button_7,3,1,2,1)
        grid_layout.addWidget(button_8,3,2,2,1)
        grid_layout.addWidget(button_9,4,0)


        v_layout = QVBoxLayout()
        v_layout.addWidget(concept_label)
        v_layout.addLayout(grid_layout)

        self.setLayout(v_layout)