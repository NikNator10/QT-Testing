from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QColorDialog, QFontDialog, QMessageBox
from PySide6.QtCore import QFile, QIODevice, QTextStream
from PySide6.QtGui import QFont, QPalette
from ui_mainwindow import Ui_MainWindow

class Mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setupUi(self)
        self.setWindowTitle("Text-Editor")

        # File
        self.actionOpen_File.triggered.connect(self.open_file)
        self.actionOpen_File.setShortcut("Ctrl+O")

        self.actionSave_File.triggered.connect(self.save_file)
        self.actionSave_File.setShortcut("Ctrl+S")

        self.actionQuit.triggered.connect(self.app.quit)
        self.actionQuit.setShortcut("Ctrl+Q")

        # Edit
        self.actionSelect_All.triggered.connect(self.text_edit.selectAll)
        self.actionSelect_All.setShortcut("Ctrl+A")

        self.actionClear_All.triggered.connect(self.text_edit.clear)
        self.actionClear_All.setShortcut("Ctrl+Del")
        
        self.actionCopy.triggered.connect(self.text_edit.copy)
        self.actionCopy.setShortcut("Ctrl+C")

        self.actionCut.triggered.connect(self.text_edit.cut)
        self.actionCut.setShortcut("Ctrl+X")

        self.actionPaste.triggered.connect(self.text_edit.paste)
        self.actionPaste.setShortcut("Ctrl+V")

        self.actionUndo.triggered.connect(self.text_edit.undo)
        self.actionUndo.setShortcut("Ctrl+Z")

        self.actionRedo.triggered.connect(self.text_edit.redo)
        self.actionRedo.setShortcut("Ctrl+Y")

        self.actionFont.triggered.connect(self.change_font)

        self.actionChange_Text_Color.triggered.connect(self.change_text_color)
        self.actionChange_Background_Color.triggered.connect(self.change_background_color)
        

        # About
        self.actionAbout_Qt.triggered.connect(QApplication.aboutQt)
        self.actionAbout.triggered.connect(self.about)



    def open_file(self):
        file_name,_ = QFileDialog.getOpenFileName(self, "Open File", "", "Text-File (*.txt);;All Files (*.*)")
        if file_name == '':
            return
        print(f"File name: {file_name}")
        file = QFile(file_name)
        if not file.open(QIODevice.ReadOnly | QIODevice.Text):
            return
        in_stream = QTextStream(file)
        file_content = ''
        while not in_stream.atEnd():
            line = in_stream.readLine()
            file_content += line
            self.text_edit.clear()
            self.text_edit.setText(file_content)
            file.close()

    def save_file(self):
        file_name,_ = QFileDialog.getSaveFileName(self, "Save File", "untitled.txt", "Text-File (*.txt);;All Files (*.*)")
        if file_name == '':
            return
        print(f"File name: {file_name}")
        file = QFile(file_name)
        
        if not file.open(QIODevice.WriteOnly | QIODevice.Text):
            return
        
        out_stream = QTextStream(file)
        out_stream << self.text_edit.toPlainText()
        file.close()

    def change_font(self):
        ok,font = QFontDialog.getFont(QFont("Arial", 20), self)
        if ok:
            self.text_edit.setCurrentFont(font)
        else:
            print("No vaild font selected")

    def change_text_color(self):
        palette = self.text_edit.palette()
        color = palette.color(QPalette.WindowText)
        chosenColor = QColorDialog.getColor(color, self, "Select Text color")
        if chosenColor.isValid():
            self.text_edit.setTextColor(chosenColor)

    def change_background_color(self):
        palette = self.text_edit.palette()
        color = palette.color(QPalette.Window)
        chosenColor = QColorDialog.getColor(color, self, "Choose Background-Color")
        if chosenColor.isValid():
            self.text_edit.setTextBackgroundColor(chosenColor)
    
    def about(self):
        QMessageBox.information(self,"Text-Editor", "Basic Text-Editor")