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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.button = QPushButton(Widget)
        self.button.setObjectName(u"button")

        self.verticalLayout_2.addWidget(self.button)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.combo_box = QComboBox(Widget)
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.setObjectName(u"combo_box")

        self.horizontalLayout.addWidget(self.combo_box)

        self.line_edit = QLineEdit(Widget)
        self.line_edit.setObjectName(u"line_edit")

        self.horizontalLayout.addWidget(self.line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.text_edit = QTextEdit(Widget)
        self.text_edit.setObjectName(u"text_edit")

        self.horizontalLayout_2.addWidget(self.text_edit)

        self.group_box = QGroupBox(Widget)
        self.group_box.setObjectName(u"group_box")
        self.verticalLayout = QVBoxLayout(self.group_box)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radio_button_1 = QRadioButton(self.group_box)
        self.radio_button_1.setObjectName(u"radio_button_1")

        self.verticalLayout.addWidget(self.radio_button_1)

        self.radio_button_2 = QRadioButton(self.group_box)
        self.radio_button_2.setObjectName(u"radio_button_2")

        self.verticalLayout.addWidget(self.radio_button_2)

        self.radio_button_3 = QRadioButton(self.group_box)
        self.radio_button_3.setObjectName(u"radio_button_3")

        self.verticalLayout.addWidget(self.radio_button_3)


        self.horizontalLayout_2.addWidget(self.group_box)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.button.setText(QCoreApplication.translate("Widget", u"Click here", None))
        self.combo_box.setItemText(0, QCoreApplication.translate("Widget", u"One", None))
        self.combo_box.setItemText(1, QCoreApplication.translate("Widget", u"Two", None))
        self.combo_box.setItemText(2, QCoreApplication.translate("Widget", u"Three", None))

        self.group_box.setTitle(QCoreApplication.translate("Widget", u"GroupBox", None))
        self.radio_button_1.setText(QCoreApplication.translate("Widget", u"RadioButton", None))
        self.radio_button_2.setText(QCoreApplication.translate("Widget", u"RadioButton", None))
        self.radio_button_3.setText(QCoreApplication.translate("Widget", u"RadioButton", None))
    # retranslateUi

