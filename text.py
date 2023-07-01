from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit, QMenuBar, QToolBar, QStatusBar, QMessageBox

class Editor(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Text-Editor LITE")

        self.text_editor = QTextEdit()
        menu_bar = QMenuBar()
        file_menu = menu_bar.addMenu("File")
        about_action = file_menu.addAction("About")
        about_action.triggered.connect(self.about)
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit)
        quit_action.setShortcut("Ctrl+q")

        tool_bar = QToolBar()
        tool_bar.addAction(quit_action)
        tool_bar.addSeparator()
        tool_bar.addAction(about_action)

        self.status_bar = QStatusBar()

        select_all = QPushButton("Select All")
        select_all.clicked.connect(self.text_editor.selectAll)

        copy = QPushButton("Copy")
        copy.clicked.connect(self.text_editor.copy)
        
        paste = QPushButton("Paste")
        paste.clicked.connect(self.text_editor.paste)

        undo = QPushButton("Undo")
        undo.clicked.connect(self.text_editor.undo)

        redo = QPushButton("Redo")
        redo.clicked.connect(self.text_editor.redo)

        console_print = QPushButton("Print to console")
        console_print.clicked.connect(self.console_print)

        h_button_layout = QHBoxLayout()
        h_button_layout.addWidget(select_all)
        h_button_layout.addWidget(copy)
        h_button_layout.addWidget(paste)
        h_button_layout.addWidget(undo)
        h_button_layout.addWidget(redo)
        h_button_layout.addWidget(console_print)

        v_layout = QVBoxLayout()
        v_layout.addWidget(menu_bar)
        v_layout.addWidget(tool_bar)
        v_layout.addLayout(h_button_layout)
        v_layout.addWidget(self.text_editor)
        v_layout.addWidget(self.status_bar)

        self.setLayout(v_layout)

    def console_print(self):
        print(self.text_editor.toPlainText())
        self.status_bar.showMessage("Text copied to console", 5000)

    def quit(self, app):
        self.app.quit()
    
    def about(self):
        QMessageBox.about(self, "About", "Text-Editor LITE V1.0")