from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QCheckBox, QGroupBox, QListWidget, QAbstractItemView, QLineEdit, QPushButton, QLabel

class Tab(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tab-Widget")

        tab = QTabWidget()

        # Checkbox - Tab
        checkbox_widget = QWidget()
        check_group = QGroupBox("Check")
        check1 = QCheckBox("Check 1")
        check2 = QCheckBox("Check 2")

        v_check_groupbox_layout = QVBoxLayout()
        v_check_groupbox_layout.addWidget(check1)
        v_check_groupbox_layout.addWidget(check2)
        check_group.setLayout(v_check_groupbox_layout)

        v_check_layout = QVBoxLayout()
        v_check_layout.addWidget(check_group)
        checkbox_widget.setLayout(v_check_layout)

        todo_widget = QWidget()
        self.todo = QListWidget()
        self.todo.setSelectionMode(QAbstractItemView.ExtendedSelection)

        # Todo - Tab
        add_todo_label = QLabel("Todo")
        self.add_todo_line_edit = QLineEdit()
        add_todo_button = QPushButton("Add Todo")
        add_todo_button.clicked.connect(self.add_todo)

        h_add_todo_layout = QHBoxLayout()
        h_add_todo_layout.addWidget(add_todo_label)
        h_add_todo_layout.addWidget(self.add_todo_line_edit)
        h_add_todo_layout.addWidget(add_todo_button)

        v_todo_layout = QVBoxLayout()    
        v_todo_layout.addWidget(self.todo)
        v_todo_layout.addLayout(h_add_todo_layout)
        todo_widget.setLayout(v_todo_layout)

        tab.addTab(check_group, "Checkbox")
        tab.addTab(todo_widget, "Todo")

        v_widget_layout = QVBoxLayout()
        v_widget_layout.addWidget(tab)
        self.setLayout(v_widget_layout)

    def add_todo(self):
        self.todo.addItem(self.add_todo_line_edit.text())