from PySide6.QtWidgets import QWidget, QPushButton, QTextEdit, QHBoxLayout, QVBoxLayout, QMenuBar, QToolBar, QMessageBox, QStatusBar
from PySide6.QtGui  import QColor
from PySide6.QtCore import Qt

class TextEditor(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Text Editor")

        # Creates the TextEdit-Widget

        self.text_editor = QTextEdit()

        # Creates a MenuBar with 3 menus and basic actions
        menu_bar = QMenuBar()

        file_menu = menu_bar.addMenu("File")
        undo_action = file_menu.addAction("Undo")
        undo_action.triggered.connect(self.text_editor.undo)
        redo_action = file_menu.addAction("Redo")
        redo_action.triggered.connect(self.text_editor.redo)
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit)
        quit_action.setShortcut("Ctrl+q")

        color_menu = menu_bar.addMenu("Text Color")
        c_black = color_menu.addAction("Black")
        c_black.triggered.connect(self.c_black)

        c_blue = color_menu.addAction("Blue")
        c_blue.triggered.connect(self.c_blue)

        c_green= color_menu.addAction("Green")
        c_green.triggered.connect(self.c_green)

        c_red = color_menu.addAction("Red")
        c_red.triggered.connect(self.c_red)

        c_yellow = color_menu.addAction("Yellow")
        c_yellow.triggered.connect(self.c_yellow)

        c_pink = color_menu.addAction("Pink")
        c_pink.triggered.connect(self.c_pink)


        cursor_size = menu_bar.addMenu("Font Size")
        fps_2 = cursor_size.addAction("2")
        fps_2.triggered.connect(self.fps_2)

        fps_2 = cursor_size.addAction("6")
        fps_2.triggered.connect(self.fps_6)

        fps_2 = cursor_size.addAction("10")
        fps_2.triggered.connect(self.fps_10)

        fps_2 = cursor_size.addAction("12")
        fps_2.triggered.connect(self.fps_12)

        fps_2 = cursor_size.addAction("20")
        fps_2.triggered.connect(self.fps_20)

        fps_2 = cursor_size.addAction("36")
        fps_2.triggered.connect(self.fps_36)

        fps_2 = cursor_size.addAction("48")
        fps_2.triggered.connect(self.fps_48)

        fps_2 = cursor_size.addAction("56")
        fps_2.triggered.connect(self.fps_56)

        fps_2 = cursor_size.addAction("72")
        fps_2.triggered.connect(self.fps_72)


        # Adds a quit and about action to the ToolBar
        tool_bar = QToolBar()

        quit_action =  tool_bar.addAction(quit_action)

        tool_bar.addSeparator()
        about_action = tool_bar.addAction("About")
        about_action.triggered.connect(self.about)
        

        self.status_bar = QStatusBar()


        # Creates zoom buttons
        zoom_in_button = QPushButton("+")
        zoom_in_button.clicked.connect(self.zoom_in)
        self.status_bar.addWidget(zoom_in_button)

        zoom_out_button = QPushButton("-")
        zoom_out_button.clicked.connect(self.zoom_out)
        self.status_bar.addWidget(zoom_out_button)

        # Creates buttons for baisc text editing
        select_all_text = QPushButton("Select all")
        select_all_text.clicked.connect(self.text_editor.selectAll)

        copy_text = QPushButton("Copy")
        copy_text.clicked.connect(self.copy_text)

        paste_text = QPushButton("Paste")
        paste_text.clicked.connect(self.text_editor.paste)

        undo_text = QPushButton("Undo")
        undo_text.clicked.connect(self.text_editor.undo)
        
        redo_text = QPushButton("Redo")
        redo_text.clicked.connect(self.text_editor.redo)

        clear_text = QPushButton("Clear Text")
        clear_text.clicked.connect(self.clear_text)

        show_current_text = QPushButton("Print Text")
        show_current_text.clicked.connect(self.current_text_print)


        # Adds all basic buttons into one horizontal_layout
        h_layout = QHBoxLayout()
        h_layout.addWidget(select_all_text)
        h_layout.addWidget(copy_text)
        h_layout.addWidget(paste_text)
        h_layout.addWidget(undo_text)
        h_layout.addWidget(redo_text)
        h_layout.addWidget(clear_text)
        h_layout.addWidget(show_current_text)

        # Combines the horizontal layout with the ToolBar/MenuBar/StatusBar/TextEditor
        v_layout = QVBoxLayout()
        v_layout.addWidget(menu_bar)
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.text_editor)
        v_layout.addWidget(tool_bar)
        v_layout.addWidget(self.status_bar)
        self.setLayout(v_layout)

    def quit(self):
        self.app.quit()

    def about(self):
        QMessageBox.about(self, "About", "Text-Editor V1.0")

    def current_text_print(self):
        print(self.text_editor.toPlainText())
        self.status_bar.showMessage("Text sent to console", 6000)

    def copy_text(self):
        self.text_editor.copy()
        self.status_bar.showMessage("Text copied to Clipboard", 6000)

    def clear_text(self):
        self.text_editor.clear()
        self.status_bar.showMessage("Text cleared!", 6000)
    def zoom_in(self):
        self.text_editor.zoomIn(1)
        
    def zoom_out(self):
        self.text_editor.zoomOut(1)

    def c_black(self):
        self.text_editor.setTextColor(QColor(0,0,0))

    def c_blue(self):
        self.text_editor.setTextColor(QColor(0,0,225))

    def c_green(self):
        self.text_editor.setTextColor(QColor(0,225,0))
    
    def c_red(self):
        self.text_editor.setTextColor(QColor(225,0,0))

    def c_yellow(self):
        self.text_editor.setTextColor(QColor(225,225,0))

    def c_pink(self):
        self.text_editor.setTextColor(QColor(255,192,203))

    def fps_2(self):
        self.text_editor.setFontPointSize(2)
        
    def fps_6(self):
        self.text_editor.setFontPointSize(6)

    def fps_10(self):
        self.text_editor.setFontPointSize(10)

    def fps_12(self):
        self.text_editor.setFontPointSize(12)

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
