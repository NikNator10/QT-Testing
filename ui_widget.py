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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(395, 301)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_1 = QPushButton(Widget)
        self.button_1.setObjectName(u"button_1")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
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

        self.button_7 = QPushButton(Widget)
        self.button_7.setObjectName(u"button_7")
        sizePolicy.setHeightForWidth(self.button_7.sizePolicy().hasHeightForWidth())
        self.button_7.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.button_7, 2, 0, 1, 1)

        self.button_8 = QPushButton(Widget)
        self.button_8.setObjectName(u"button_8")
        sizePolicy.setHeightForWidth(self.button_8.sizePolicy().hasHeightForWidth())
        self.button_8.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.button_8, 2, 1, 1, 1)

        self.button_9 = QPushButton(Widget)
        self.button_9.setObjectName(u"button_9")
        sizePolicy.setHeightForWidth(self.button_9.sizePolicy().hasHeightForWidth())
        self.button_9.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.button_9, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.save_color_button = QPushButton(Widget)
        self.save_color_button.setObjectName(u"save_color_button")

        self.horizontalLayout.addWidget(self.save_color_button)

        self.load_color_button = QPushButton(Widget)
        self.load_color_button.setObjectName(u"load_color_button")

        self.horizontalLayout.addWidget(self.load_color_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.button_1.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.button_2.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.button_3.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.button_4.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.button_5.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.button_6.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.button_7.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.button_8.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.button_9.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.save_color_button.setText(QCoreApplication.translate("Widget", u"Save color", None))
        self.load_color_button.setText(QCoreApplication.translate("Widget", u"Load color", None))
    # retranslateUi

