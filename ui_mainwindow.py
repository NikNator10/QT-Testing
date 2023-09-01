# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTextEdit, QToolBar,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionOpen_File = QAction(MainWindow)
        self.actionOpen_File.setObjectName(u"actionOpen_File")
        self.actionSave_File = QAction(MainWindow)
        self.actionSave_File.setObjectName(u"actionSave_File")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon = QIcon()
        icon.addFile(u":/images/quitIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionQuit.setIcon(icon)
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        icon1 = QIcon()
        icon1.addFile(u":/images/copyIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCopy.setIcon(icon1)
        self.actionCut = QAction(MainWindow)
        self.actionCut.setObjectName(u"actionCut")
        icon2 = QIcon()
        icon2.addFile(u":/images/cutIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCut.setIcon(icon2)
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        icon3 = QIcon()
        icon3.addFile(u":/images/pasteIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPaste.setIcon(icon3)
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        icon4 = QIcon()
        icon4.addFile(u":/images/undoIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionUndo.setIcon(icon4)
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        icon5 = QIcon()
        icon5.addFile(u":/images/redoIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRedo.setIcon(icon5)
        self.actionClear_All = QAction(MainWindow)
        self.actionClear_All.setObjectName(u"actionClear_All")
        icon6 = QIcon()
        icon6.addFile(u":/images/clearIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionClear_All.setIcon(icon6)
        self.actionSelect_All = QAction(MainWindow)
        self.actionSelect_All.setObjectName(u"actionSelect_All")
        icon7 = QIcon()
        icon7.addFile(u":/images/selectIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSelect_All.setIcon(icon7)
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        icon8 = QIcon()
        icon8.addFile(u":/images/aboutQtIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout_Qt.setIcon(icon8)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon9 = QIcon()
        icon9.addFile(u":/images/aboutIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon9)
        self.actionFont = QAction(MainWindow)
        self.actionFont.setObjectName(u"actionFont")
        icon10 = QIcon()
        icon10.addFile(u":/images/fontIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionFont.setIcon(icon10)
        self.actionChange_Text_Color = QAction(MainWindow)
        self.actionChange_Text_Color.setObjectName(u"actionChange_Text_Color")
        icon11 = QIcon()
        icon11.addFile(u":/images/text_colorIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionChange_Text_Color.setIcon(icon11)
        self.actionChange_Background_Color = QAction(MainWindow)
        self.actionChange_Background_Color.setObjectName(u"actionChange_Background_Color")
        icon12 = QIcon()
        icon12.addFile(u":/images/background_colorIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionChange_Background_Color.setIcon(icon12)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.text_edit = QTextEdit(self.centralwidget)
        self.text_edit.setObjectName(u"text_edit")

        self.verticalLayout.addWidget(self.text_edit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionSave_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuEdit.addAction(self.actionClear_All)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFont)
        self.menuEdit.addAction(self.actionChange_Text_Color)
        self.menuEdit.addAction(self.actionChange_Background_Color)
        self.menuAbout.addAction(self.actionAbout_Qt)
        self.menuAbout.addAction(self.actionAbout)
        self.toolBar.addAction(self.actionQuit)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSelect_All)
        self.toolBar.addAction(self.actionClear_All)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionFont)
        self.toolBar.addAction(self.actionChange_Background_Color)
        self.toolBar.addAction(self.actionChange_Text_Color)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen_File.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.actionSave_File.setText(QCoreApplication.translate("MainWindow", u"Save File", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.actionCut.setText(QCoreApplication.translate("MainWindow", u"Cut", None))
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.actionClear_All.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
        self.actionSelect_All.setText(QCoreApplication.translate("MainWindow", u"Select All", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionFont.setText(QCoreApplication.translate("MainWindow", u"Change Font Size/Color", None))
        self.actionChange_Text_Color.setText(QCoreApplication.translate("MainWindow", u"Change Text Color", None))
        self.actionChange_Background_Color.setText(QCoreApplication.translate("MainWindow", u"Change Background Color", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

