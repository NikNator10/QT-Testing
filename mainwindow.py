from PySide6.QtWidgets import QApplication, QMainWindow, QFontDialog, QColorDialog, QMessageBox
from PySide6.QtGui import QFont, QPalette
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setupUi(self)
        self.setWindowTitle("Text - Editor")

        self.actionQuit.triggered.connect(self.app.quit)

        self.actionSelect_All.triggered.connect(self.text_edit.selectAll)
        self.actionCopy.triggered.connect(self.text_edit.copy)
        self.actionPaste.triggered.connect(self.text_edit.paste)
        self.actionCut.triggered.connect(self.text_edit.cut)
        
        self.actionClear_All.triggered.connect(self.text_edit.clear)

        self.actionUndo.triggered.connect(self.text_edit.undo)
        self.actionRedo.triggered.connect(self.text_edit.redo)

        self.actionEdit_Font.triggered.connect(self.edit_font)
        self.actionEdit_textColor.triggered.connect(self.edit_text_color)
        self.actionEdit_backgroundColor.triggered.connect(self.edit_background_color)

        self.actionAbout_Qt.triggered.connect(QApplication.aboutQt)
        self.actionAbout.triggered.connect(self.about)

    def edit_font(self):
        ok,font = QFontDialog.getFont(QFont("Arial", 20), self)
        if ok:
            self.text_edit.setCurrentFont(font)
        else:
            print("No font selected")
    
    def edit_text_color(self):
        palette = self.text_edit.palette()
        color = palette.color(QPalette.WindowText)
        chosenColor = QColorDialog.getColor(color, self, "Select Color")

        if chosenColor.isValid():
             self.text_edit.setTextColor(chosenColor)

    def about(self):
        QMessageBox.information(self, "About", "Text-Editor")




    def edit_background_color(self):
        palette = self.text_edit.palette()
        color = palette.color(QPalette.Window)
        chosenColor = QColorDialog.getColor(color, self, "Select background color")
   
        if chosenColor.isValid():
                self.text_edit.setTextBackgroundColor(chosenColor)
        else:
                print("No valid color selected")