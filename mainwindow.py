from PySide6.QtWidgets import QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        self.setWindowTitle("Basic Text-Editor")

        self.actionQuit.triggered.connect(self.quit)
        self.actionCopy.triggered.connect(self.copy)
        self.actionCut.triggered.connect(self.cut)
        self.actionPaste.triggered.connect(self.paste)
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionAbout.triggered.connect(self.about)
        self.actionAbout_Qt.triggered.connect(self.about_qt)

    def quit(self):
        self.app.quit()
    def copy(self):
        self.text_edit.copy()
    def cut(self):
        self.text_edit.cut()
    def paste(self):
        self.text_edit.paste()
    def undo(self):
        self.text_edit.undo()
    def redo(self):
        self.text_edit.redo()
    def about(self):
        QMessageBox.about(self,"Basic Text-Editor", "Text-Editor with icons")
    def about_qt(self):
        QMessageBox.aboutQt(self)
    