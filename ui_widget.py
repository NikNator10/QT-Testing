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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(663, 500)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.todo_list_widget = QListWidget(Widget)
        self.todo_list_widget.setObjectName(u"todo_list_widget")
        font = QFont()
        font.setPointSize(12)
        self.todo_list_widget.setFont(font)

        self.verticalLayout.addWidget(self.todo_list_widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.add_todo_line_edit = QLineEdit(Widget)
        self.add_todo_line_edit.setObjectName(u"add_todo_line_edit")

        self.horizontalLayout.addWidget(self.add_todo_line_edit)

        self.add_todo_button = QPushButton(Widget)
        self.add_todo_button.setObjectName(u"add_todo_button")

        self.horizontalLayout.addWidget(self.add_todo_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Todo:", None))
        self.add_todo_button.setText(QCoreApplication.translate("Widget", u"Add Todo", None))
    # retranslateUi

