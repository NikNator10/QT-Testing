from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QRadioButton, QCheckBox, QGroupBox, QButtonGroup

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QRadioButton, QCheckBox & QGroupBox")

        # Creates a group with 3 checkboxes
        todos = QGroupBox("Todos")
        todo_1 = QCheckBox("Learn QT")
        todo_2 = QCheckBox("Install Ubuntu")
        todo_3 = QCheckBox("Learn Premiere Pro")

        # Assigns a layout to the group
        todo_layout = QVBoxLayout()
        todo_layout.addWidget(todo_1)
        todo_layout.addWidget(todo_2)
        todo_layout.addWidget(todo_3)
        todos.setLayout(todo_layout)


        fav_os = QGroupBox("Favourite Desktop OS")
        win = QCheckBox("Windows")
        mac = QCheckBox("Mac")
        linux = QCheckBox("Linux")
        linux.setChecked(True)

        # Creates exclusive checkboxes
        exclusive_fav_os = QButtonGroup(self)
        exclusive_fav_os.addButton(win)
        exclusive_fav_os.addButton(mac)
        exclusive_fav_os.addButton(linux)

        layout_fav_os = QVBoxLayout()
        layout_fav_os.addWidget(win)
        layout_fav_os.addWidget(mac)
        layout_fav_os.addWidget(linux)
        fav_os.setLayout(layout_fav_os)

        # Creates a group with 4 radio buttons (exclusive)
        fav_mobile_os = QGroupBox("Favourite Mobile OS")
        android = QRadioButton("Android")
        ios = QRadioButton("iOS")
        ubuntu_mobile = QRadioButton("Ubuntu Touch")
        win_m = QRadioButton("Windows Mobile")

        layout_fav_mobile_os = QVBoxLayout()
        layout_fav_mobile_os.addWidget(android)
        layout_fav_mobile_os.addWidget(ios)
        layout_fav_mobile_os.addWidget(ubuntu_mobile)
        layout_fav_mobile_os.addWidget(win_m)
        fav_mobile_os.setLayout(layout_fav_mobile_os)


        h_layout = QHBoxLayout()
        h_layout.addWidget(todos)
        h_layout.addWidget(fav_os)
        

        # Combines everything into a bigger layout
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(fav_mobile_os)

        self.setLayout(v_layout)