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
        Widget.resize(203, 141)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.get_item_button = QPushButton(Widget)
        self.get_item_button.setObjectName(u"get_item_button")

        self.verticalLayout.addWidget(self.get_item_button)

        self.get_int_button = QPushButton(Widget)
        self.get_int_button.setObjectName(u"get_int_button")

        self.verticalLayout.addWidget(self.get_int_button)

        self.get_double_button = QPushButton(Widget)
        self.get_double_button.setObjectName(u"get_double_button")

        self.verticalLayout.addWidget(self.get_double_button)

        self.get_text_button = QPushButton(Widget)
        self.get_text_button.setObjectName(u"get_text_button")

        self.verticalLayout.addWidget(self.get_text_button)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.get_item_button.setText(QCoreApplication.translate("Widget", u"getItem", None))
        self.get_int_button.setText(QCoreApplication.translate("Widget", u"getInt", None))
        self.get_double_button.setText(QCoreApplication.translate("Widget", u"getDouble", None))
        self.get_text_button.setText(QCoreApplication.translate("Widget", u"getText", None))
    # retranslateUi

