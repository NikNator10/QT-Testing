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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(514, 495)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_1 = QPushButton(Widget)
        self.button_1.setObjectName(u"button_1")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_1.sizePolicy().hasHeightForWidth())
        self.button_1.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.button_1, 0, 0, 1, 1)

        self.button_2 = QPushButton(Widget)
        self.button_2.setObjectName(u"button_2")
        sizePolicy.setHeightForWidth(self.button_2.sizePolicy().hasHeightForWidth())
        self.button_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.button_2, 0, 1, 1, 1)

        self.button_3 = QPushButton(Widget)
        self.button_3.setObjectName(u"button_3")
        sizePolicy.setHeightForWidth(self.button_3.sizePolicy().hasHeightForWidth())
        self.button_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.button_3, 0, 2, 1, 1)

        self.button_4 = QPushButton(Widget)
        self.button_4.setObjectName(u"button_4")
        sizePolicy.setHeightForWidth(self.button_4.sizePolicy().hasHeightForWidth())
        self.button_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.button_4, 1, 0, 1, 1)

        self.button_5 = QPushButton(Widget)
        self.button_5.setObjectName(u"button_5")
        sizePolicy.setHeightForWidth(self.button_5.sizePolicy().hasHeightForWidth())
        self.button_5.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.button_5, 1, 1, 1, 1)

        self.button_6 = QPushButton(Widget)
        self.button_6.setObjectName(u"button_6")
        sizePolicy.setHeightForWidth(self.button_6.sizePolicy().hasHeightForWidth())
        self.button_6.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.button_6, 1, 2, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.save_color_button = QPushButton(Widget)
        self.save_color_button.setObjectName(u"save_color_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.save_color_button.sizePolicy().hasHeightForWidth())
        self.save_color_button.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.save_color_button)

        self.load_color_button = QPushButton(Widget)
        self.load_color_button.setObjectName(u"load_color_button")
        sizePolicy1.setHeightForWidth(self.load_color_button.sizePolicy().hasHeightForWidth())
        self.load_color_button.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.load_color_button)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.button_1.setText(QCoreApplication.translate("Widget", u"Button 1", None))
        self.button_2.setText(QCoreApplication.translate("Widget", u"Button 2", None))
        self.button_3.setText(QCoreApplication.translate("Widget", u"Button 3", None))
        self.button_4.setText(QCoreApplication.translate("Widget", u"Button 4", None))
        self.button_5.setText(QCoreApplication.translate("Widget", u"Button 5", None))
        self.button_6.setText(QCoreApplication.translate("Widget", u"Button 6", None))
        self.save_color_button.setText(QCoreApplication.translate("Widget", u"Save Color", None))
        self.load_color_button.setText(QCoreApplication.translate("Widget", u"Load Color", None))
    # retranslateUi

