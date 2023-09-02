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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(480, 147)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.src_line_edit = QLineEdit(Widget)
        self.src_line_edit.setObjectName(u"src_line_edit")

        self.horizontalLayout.addWidget(self.src_line_edit)

        self.choose_file_button = QPushButton(Widget)
        self.choose_file_button.setObjectName(u"choose_file_button")

        self.horizontalLayout.addWidget(self.choose_file_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dst_line_edit = QLineEdit(Widget)
        self.dst_line_edit.setObjectName(u"dst_line_edit")

        self.horizontalLayout_2.addWidget(self.dst_line_edit)

        self.copy_button = QPushButton(Widget)
        self.copy_button.setObjectName(u"copy_button")

        self.horizontalLayout_2.addWidget(self.copy_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.choose_file_button.setText(QCoreApplication.translate("Widget", u"Choose File", None))
        self.copy_button.setText(QCoreApplication.translate("Widget", u"Copy", None))
    # retranslateUi

