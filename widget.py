from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QGridLayout, QHBoxLayout, QPushButton, QRadioButton, QGroupBox, QMenuBar, QMessageBox

class Editor(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.setWindowTitle("Text-Editor with radio buttons")


        self.text_editor = QTextEdit()

        select_all = QPushButton("Select All")
        select_all.clicked.connect(self.text_editor.selectAll)
        copy = QPushButton("Copy")
        copy.clicked.connect(self.text_editor.copy)
        cut = QPushButton("Cut")
        cut.clicked.connect(self.text_editor.cut)
        paste = QPushButton("Paste")
        paste.clicked.connect(self.text_editor.paste)
        clear = QPushButton("Clear All")
        clear.clicked.connect(self.text_editor.clear)
        undo = QPushButton("Undo")
        undo.clicked.connect(self.text_editor.undo)
        redo = QPushButton("Redo")
        redo.clicked.connect(self.text_editor.redo)

        menu_bar = QMenuBar()
        file_menu = menu_bar.addMenu("File")

        select_all_action = file_menu.addAction("Select All")
        select_all_action.triggered.connect(self.text_editor.selectAll)
        select_all_action.setShortcut("Ctrl+a")

        clear_action = file_menu.addAction("Clear Text")
        clear_action.triggered.connect(self.text_editor.clear)
        clear_action.setShortcut("Ctrl+del")

        copy_action = file_menu.addAction("Copy")
        copy_action.triggered.connect(self.text_editor.copy)
        copy_action.setShortcut("Ctrl+c")

        cut_action = file_menu.addAction("Cut")
        cut_action.triggered.connect(self.text_editor.cut)
        cut_action.setShortcut("Ctrl+x")

        paste_action = file_menu.addAction("Paste")
        paste_action.triggered.connect(self.text_editor.paste)
        paste_action.setShortcut("Ctrl+v")

        undo_action = file_menu.addAction("Undo")
        undo_action.triggered.connect(self.text_editor.undo)
        undo_action.setShortcut("Ctrl+z")

        redo_action = file_menu.addAction("Redo")
        redo_action.triggered.connect(self.text_editor.redo)
        redo_action.setShortcut("Ctrl+y")

        about_action = file_menu.addAction("About")
        about_action.triggered.connect(self.about)

        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit)
        quit_action.setShortcut("Ctrl+q")

        font_size = QGroupBox("Font Size")

        fps_2 = QRadioButton("2")
        fps_2.toggled.connect(self.fps_2)

        fps_6 = QRadioButton("6")
        fps_6.toggled.connect(self.fps_6)

        fps_10 = QRadioButton("10")
        fps_10.toggled.connect(self.fps_10)

        fps_12 = QRadioButton("12")
        fps_12.toggled.connect(self.fps_12)

        fps_16 = QRadioButton("16")
        fps_16.toggled.connect(self.fps_16)
    
        fps_20 = QRadioButton("20")
        fps_20.toggled.connect(self.fps_20)

        fps_36 = QRadioButton("36")
        fps_36.toggled.connect(self.fps_36)

        fps_48 = QRadioButton("48")
        fps_48.toggled.connect(self.fps_48)
 
        fps_56 = QRadioButton("56")
        fps_56.toggled.connect(self.fps_56)

        fps_72 = QRadioButton("72")
        fps_72.toggled.connect(self.fps_72)
                            
        font_size_layout = QGridLayout()
        font_size_layout.addWidget(fps_2,0,0)
        font_size_layout.addWidget(fps_6,1,0)
        font_size_layout.addWidget(fps_10,2,0)
        font_size_layout.addWidget(fps_12,3,0)
        font_size_layout.addWidget(fps_16,4,0)

        font_size_layout.addWidget(fps_20,0,1)
        font_size_layout.addWidget(fps_36,1,1)  
        font_size_layout.addWidget(fps_48,2,1)
        font_size_layout.addWidget(fps_56,3,1)
        font_size_layout.addWidget(fps_72,4,1)         
        font_size.setLayout(font_size_layout)

        button_layout = QHBoxLayout()
        button_layout.addWidget(select_all)
        button_layout.addWidget(copy)
        button_layout.addWidget(cut)
        button_layout.addWidget(paste)
        button_layout.addWidget(clear)
        button_layout.addWidget(undo)
        button_layout.addWidget(redo)

        v_layout = QVBoxLayout()
        v_layout.addWidget(menu_bar)
        v_layout.addLayout(button_layout)
        v_layout.addWidget(self.text_editor)
        v_layout.addWidget(font_size)
        self.setLayout(v_layout)

    def quit(self):
        self.app.quit()

    def about(self):
        QMessageBox.about(self,"About", "Text-Editor with radio buttons")

    
    def fps_2(self):
        self.text_editor.setFontPointSize(2)

    def fps_6(self):
        self.text_editor.setFontPointSize(6)

    def fps_10(self):
        self.text_editor.setFontPointSize(10)

    def fps_12(self):
        self.text_editor.setFontPointSize(12)

    def fps_16(self):
        self.text_editor.setFontPointSize(16)

    def fps_20(self):
        self.text_editor.setFontPointSize(20)

    def fps_36(self):
        self.text_editor.setFontPointSize(36)

    def fps_48(self):
        self.text_editor.setFontPointSize(48)

    def fps_56(self):
        self.text_editor.setFontPointSize(56)


    def fps_72(self):
        self.text_editor.setFontPointSize(72)