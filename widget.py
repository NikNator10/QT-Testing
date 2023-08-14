from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QLabel, QLineEdit

class Combo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Todo-Application with QComboBox")

        self.todo_combo = QComboBox()
        self.todo_combo.setPlaceholderText("Your Todos will appear here")

        # Add a todo
        add_todo_label = QLabel("Todo: ")
        self.add_todo_line_edit = QLineEdit()
        add_todo_button = QPushButton("Add Todo")
        add_todo_button.clicked.connect(self.add_todo)
        
        # Layout for adding todos
        h_add_todo_layout = QHBoxLayout()
        h_add_todo_layout.addWidget(add_todo_label)
        h_add_todo_layout.addWidget(self.add_todo_line_edit)
        h_add_todo_layout.addWidget(add_todo_button)

        # Delete selected todos
        delete_todo = QPushButton("Delete selected Todo")
        delete_todo.clicked.connect(self.delete_todo)

        # Clear all todos
        clear_todo = QPushButton("Clear all Todos")
        clear_todo.clicked.connect(self.clear_todo)

        # List current todo
        list_current_todo = QPushButton("List current Todo")
        list_current_todo.clicked.connect(self.list_current_todo)

    	# List all todos
        list_all_todo = QPushButton("List all Todos")
        list_all_todo.clicked.connect(self.list_all_todo)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.todo_combo)
        v_layout.addLayout(h_add_todo_layout)
        v_layout.addWidget(delete_todo)
        v_layout.addWidget(clear_todo)
        v_layout.addWidget(list_current_todo)
        v_layout.addWidget(list_all_todo)
        self.setLayout(v_layout)

    def add_todo(self):
        self.todo_combo.addItem(self.add_todo_line_edit.text())

    def delete_todo(self):
        self.todo_combo.removeItem(self.todo_combo.currentIndex())

    def clear_todo(self):
        self.todo_combo.clear()

    def list_current_todo(self):
        print("Current Item: ", self.todo_combo.currentText(),"\nCurrent Index: ", self.todo_combo.currentIndex())
    
    def list_all_todo(self):
        for i in range(self.todo_combo.count()):
            print(f"[{i}] - {self.todo_combo.itemText(i)}")