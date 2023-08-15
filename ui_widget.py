# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(919, 457)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.text_edit = QTextEdit(Widget)
        self.text_edit.setObjectName(u"text_edit")

        self.horizontalLayout.addWidget(self.text_edit)

        self.verticalSpacer = QSpacerItem(20, 436, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.select_all_button = QPushButton(Widget)
        self.select_all_button.setObjectName(u"select_all_button")

        self.verticalLayout.addWidget(self.select_all_button)

        self.copy_button = QPushButton(Widget)
        self.copy_button.setObjectName(u"copy_button")

        self.verticalLayout.addWidget(self.copy_button)

        self.paste_button = QPushButton(Widget)
        self.paste_button.setObjectName(u"paste_button")

        self.verticalLayout.addWidget(self.paste_button)

        self.undo_button = QPushButton(Widget)
        self.undo_button.setObjectName(u"undo_button")

        self.verticalLayout.addWidget(self.undo_button)

        self.redo_button = QPushButton(Widget)
        self.redo_button.setObjectName(u"redo_button")

        self.verticalLayout.addWidget(self.redo_button)

        self.clear_button = QPushButton(Widget)
        self.clear_button.setObjectName(u"clear_button")

        self.verticalLayout.addWidget(self.clear_button)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.select_all_button.setText(QCoreApplication.translate("Widget", u"Select All", None))
        self.copy_button.setText(QCoreApplication.translate("Widget", u"Copy", None))
        self.paste_button.setText(QCoreApplication.translate("Widget", u"Paste", None))
        self.undo_button.setText(QCoreApplication.translate("Widget", u"Undo", None))
        self.redo_button.setText(QCoreApplication.translate("Widget", u"Redo", None))
        self.clear_button.setText(QCoreApplication.translate("Widget", u"Clear", None))
    # retranslateUi

