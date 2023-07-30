from PySide6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QAbstractItemView, QListWidget, QLabel, QLineEdit, QToolBar, QStatusBar, QMessageBox

class Todo(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        
        self.setWindowTitle("Basic Todo-Application")

        self.todo = QListWidget()
        self.todo.setSelectionMode(QAbstractItemView.ExtendedSelection)

        label_add_todo = QLabel("Add Todo: ")
        self.line_add_todo = QLineEdit()
        button_add_todo = QPushButton("Add Todo")
        button_add_todo.clicked.connect(self.add_todo)

        button_delete_todo = QPushButton("Delete current Todo")
        button_delete_todo.clicked.connect(self.delete_todo)

        button_clear_all = QPushButton("Delete all Todos")
        button_clear_all.clicked.connect(self.clear_todo_list)

        button_todo_print = QPushButton("Print selected Todos to Console")
        button_todo_print.clicked.connect(self.print_todos)


        tool_bar = QToolBar()
        quit_action = tool_bar.addAction("Quit")
        quit_action.triggered.connect(self.quit)
        quit_action.setShortcut("Ctrl+q")

        about_action = tool_bar.addAction("About")
        about_action.triggered.connect(self.about)

        self.status_bar = QStatusBar()       

        self.todo.currentItemChanged.connect(self.current_todo)

        todo_layout = QHBoxLayout()
        todo_layout.addWidget(label_add_todo)
        todo_layout.addWidget(self.line_add_todo)
        todo_layout.addWidget(button_add_todo)

        button_layout = QGridLayout()
        button_layout.addWidget(button_delete_todo,0,0)
        button_layout.addWidget(button_clear_all,0,1)
        button_layout.addWidget(button_todo_print,1,0,1,2)
        
        v_layout = QVBoxLayout()
        v_layout.addWidget(tool_bar)
        v_layout.addWidget(self.todo)
        v_layout.addLayout(todo_layout)
        v_layout.addLayout(button_layout)
        v_layout.addWidget(self.status_bar)
        self.setLayout(v_layout)

    def add_todo(self):
        self.todo.addItem(self.line_add_todo.text())

    def delete_todo(self):
        self.todo.takeItem(self.todo.currentRow())

    def clear_todo_list(self):
        self.todo.clear()

    def print_todos(self):
        list = self.todo.selectedItems()
        for i in list:
            print(i.text())
    
    def current_todo(self, todo):
        self.status_bar.showMessage("Current Todo : " + todo.text())

    def quit(self,app):
        self.app.quit()

    def about(self):
        QMessageBox.about(self, "About", "Basic Todo-Application V1.0")