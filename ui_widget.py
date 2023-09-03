# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(550, 359)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.text_edit = QTextEdit(Widget)
        self.text_edit.setObjectName(u"text_edit")

        self.horizontalLayout.addWidget(self.text_edit)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.open_file_button = QPushButton(Widget)
        self.open_file_button.setObjectName(u"open_file_button")

        self.verticalLayout.addWidget(self.open_file_button)

        self.save_file_button = QPushButton(Widget)
        self.save_file_button.setObjectName(u"save_file_button")

        self.verticalLayout.addWidget(self.save_file_button)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.open_file_button.setText(QCoreApplication.translate("Widget", u"Open File", None))
        self.save_file_button.setText(QCoreApplication.translate("Widget", u"Save File", None))
    # retranslateUi

