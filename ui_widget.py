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
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(456, 466)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.text_edit = QTextEdit(Widget)
        self.text_edit.setObjectName(u"text_edit")

        self.horizontalLayout.addWidget(self.text_edit)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.save_file_button = QPushButton(Widget)
        self.save_file_button.setObjectName(u"save_file_button")

        self.verticalLayout.addWidget(self.save_file_button)

        self.open_file_button = QPushButton(Widget)
        self.open_file_button.setObjectName(u"open_file_button")

        self.verticalLayout.addWidget(self.open_file_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.source_line_edit = QLineEdit(Widget)
        self.source_line_edit.setObjectName(u"source_line_edit")

        self.horizontalLayout_3.addWidget(self.source_line_edit)

        self.select_file_button = QPushButton(Widget)
        self.select_file_button.setObjectName(u"select_file_button")

        self.horizontalLayout_3.addWidget(self.select_file_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.destination_line_edit = QLineEdit(Widget)
        self.destination_line_edit.setObjectName(u"destination_line_edit")

        self.horizontalLayout_2.addWidget(self.destination_line_edit)

        self.copy_file_button = QPushButton(Widget)
        self.copy_file_button.setObjectName(u"copy_file_button")

        self.horizontalLayout_2.addWidget(self.copy_file_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.save_file_button.setText(QCoreApplication.translate("Widget", u"Save File", None))
        self.open_file_button.setText(QCoreApplication.translate("Widget", u"Open File", None))
        self.select_file_button.setText(QCoreApplication.translate("Widget", u"Select FIle", None))
        self.copy_file_button.setText(QCoreApplication.translate("Widget", u"Copy File", None))
    # retranslateUi

