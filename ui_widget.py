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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(400, 132)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.get_existing_directory_button = QPushButton(Widget)
        self.get_existing_directory_button.setObjectName(u"get_existing_directory_button")

        self.verticalLayout.addWidget(self.get_existing_directory_button)

        self.get_open_file_name = QPushButton(Widget)
        self.get_open_file_name.setObjectName(u"get_open_file_name")

        self.verticalLayout.addWidget(self.get_open_file_name)

        self.get_open_file_names = QPushButton(Widget)
        self.get_open_file_names.setObjectName(u"get_open_file_names")

        self.verticalLayout.addWidget(self.get_open_file_names)

        self.get_save_file_name_button = QPushButton(Widget)
        self.get_save_file_name_button.setObjectName(u"get_save_file_name_button")

        self.verticalLayout.addWidget(self.get_save_file_name_button)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.get_existing_directory_button.setText(QCoreApplication.translate("Widget", u"getExistingDirectory", None))
        self.get_open_file_name.setText(QCoreApplication.translate("Widget", u"getOpenFileName  ", None))
        self.get_open_file_names.setText(QCoreApplication.translate("Widget", u"getOpenFileNames", None))
        self.get_save_file_name_button.setText(QCoreApplication.translate("Widget", u"getSaveFileName", None))
    # retranslateUi

