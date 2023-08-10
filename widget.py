from PySide6.QtWidgets import QWidget, QTabWidget, QListWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QButtonGroup, QGroupBox, QRadioButton, QCheckBox, QAbstractItemView

class Tab(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.setWindowTitle("Tab-Application")
        
        tab_widget = QTabWidget(self)


        # Text-Editor
        text_tab = QWidget()
        self.text = QTextEdit()

        select_all = QPushButton("Select All")
        select_all.clicked.connect(self.select_all)

        copy = QPushButton("Copy")
        copy.clicked.connect(self.copy)

        paste = QPushButton("Paste")
        paste.clicked.connect(self.paste)

        cut = QPushButton("Cut")
        cut.clicked.connect(self.cut)

        h_textbuttonlayout = QHBoxLayout()
        h_textbuttonlayout.addWidget(select_all)
        h_textbuttonlayout.addWidget(copy)
        h_textbuttonlayout.addWidget(paste)
        h_textbuttonlayout.addWidget(cut)

        v_textlayout = QVBoxLayout()
        v_textlayout.addWidget(self.text)
        v_textlayout.addLayout(h_textbuttonlayout)
        text_tab.setLayout(v_textlayout)

        # Todo-Application
        todo_tab = QWidget()
        self.todo = QListWidget()

        self.todo.setSelectionMode(QAbstractItemView.ExtendedSelection)

        label_new_todo = QLabel("New Todo: ")
        self.line_edit_new_todo = QLineEdit()
        button_new_todo = QPushButton("Add Todo")
        button_new_todo.clicked.connect(self.add_todo)

        button_delete_todo = QPushButton("Delete Todo")
        button_delete_todo.clicked.connect(self.delete_todo)
        
        button_clear_all_todo = QPushButton("Clear all Todos")
        button_clear_all_todo.clicked.connect(self.clear_todos)

        print_todos = QPushButton("Print selected Todos to Terminal")
        print_todos.clicked.connect(self.print_todos)

        h_add_todolayout = QHBoxLayout()
        h_add_todolayout.addWidget(label_new_todo)
        h_add_todolayout.addWidget(self.line_edit_new_todo)
        h_add_todolayout.addWidget(button_new_todo)

        h_todo_buttons = QHBoxLayout()
        h_todo_buttons.addWidget(button_delete_todo)
        h_todo_buttons.addWidget(button_clear_all_todo)
        
        v_todolayout = QVBoxLayout()
        v_todolayout.addWidget(self.todo)
        v_todolayout.addLayout(h_add_todolayout)
        v_todolayout.addLayout(h_todo_buttons)
        v_todolayout.addWidget(print_todos)
        todo_tab.setLayout(v_todolayout)

        # Checkbox and Radiobuttons
        check_tab = QWidget()

        group_check = QGroupBox("Checkboxes")
        check_1 = QCheckBox("Box 1")
        check_2 = QCheckBox("Box 2")
        check_3 = QCheckBox("Box 3")
        check_4 = QCheckBox("Box 4")

        v_check_layout = QVBoxLayout()
        v_check_layout.addWidget(check_1)
        v_check_layout.addWidget(check_2)
        v_check_layout.addWidget(check_3)        
        v_check_layout.addWidget(check_4)
        group_check.setLayout(v_check_layout)

        group_radio = QGroupBox("Radiobuttons")
        radio_1 = QRadioButton("Radio 1")
        radio_2 = QRadioButton("Radio 2")
        radio_3 = QRadioButton("Radio 3")
        radio_4 = QRadioButton("Radio 4")        

        v_radio_layout = QVBoxLayout()
        v_radio_layout.addWidget(radio_1)
        v_radio_layout.addWidget(radio_2)
        v_radio_layout.addWidget(radio_3)
        v_radio_layout.addWidget(radio_4)
        group_radio.setLayout(v_radio_layout)

        # Exclusive Checkboxes
        group_ex_check = QGroupBox("Exclusive Checkboxes")
        ex_check_1 = QCheckBox("Ex Check 1")
        ex_check_1.setChecked(True)
        ex_check_2 = QCheckBox("Ex Check 2")
        ex_check_3 = QCheckBox("Ex Check 3")
        ex_check_4 = QCheckBox("Ex Check 4")

        ex_button_group = QButtonGroup(self)
        ex_button_group.addButton(ex_check_1)
        ex_button_group.addButton(ex_check_2)
        ex_button_group.addButton(ex_check_3)
        ex_button_group.addButton(ex_check_4)

        v_ex_layout = QVBoxLayout()
        v_ex_layout.addWidget(ex_check_1)
        v_ex_layout.addWidget(ex_check_2)
        v_ex_layout.addWidget(ex_check_3)
        v_ex_layout.addWidget(ex_check_4)
        group_ex_check.setLayout(v_ex_layout)

        # Creates Layout for check_tab
        check_tab_layout = QGridLayout()
        check_tab_layout.addWidget(group_check,0,0)
        check_tab_layout.addWidget(group_radio,0,1)
        check_tab_layout.addWidget(group_ex_check,1,0)
        check_tab.setLayout(check_tab_layout)

        # Adds single tabs to the tab widget
        tab_widget.addTab(text_tab, "Basic Text-Editor")
        tab_widget.addTab(todo_tab, "Basic Todo-Application")
        tab_widget.addTab(check_tab, "Checkboxes and Radiobuttons")

    	# Adds the tab widget to a layout
        layout = QHBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)



    # Text-Editor
    def select_all(self):
        self.text.selectAll()

    def copy(self):
        self.text.copy()
    
    def paste(self):
        self.text.paste()

    def cut(self):
        self.text.cut()

    # Todo
    def add_todo(self):
        self.todo.addItem(self.line_edit_new_todo.text())

    def delete_todo(self):
        self.todo.takeItem(self.todo.currentRow())

    def clear_todos(self):
        self.todo.clear()

    def print_todos(self):
        list = self.todo.selectedItems()
        for i in list:
            print(i.text())