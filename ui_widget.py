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
        Widget.resize(428, 414)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(Widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.button_1 = QPushButton(Widget)
        self.button_1.setObjectName(u"button_1")

        self.verticalLayout_3.addWidget(self.button_1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radio_button_1 = QRadioButton(self.groupBox)
        self.radio_button_1.setObjectName(u"radio_button_1")

        self.verticalLayout.addWidget(self.radio_button_1)

        self.radio_button_2 = QRadioButton(self.groupBox)
        self.radio_button_2.setObjectName(u"radio_button_2")

        self.verticalLayout.addWidget(self.radio_button_2)

        self.radio_button_3 = QRadioButton(self.groupBox)
        self.radio_button_3.setObjectName(u"radio_button_3")

        self.verticalLayout.addWidget(self.radio_button_3)


        self.horizontalLayout.addWidget(self.groupBox)

        self.textEdit = QTextEdit(Widget)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout.addWidget(self.textEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.line_edit = QLineEdit(Widget)
        self.line_edit.setObjectName(u"line_edit")

        self.verticalLayout_2.addWidget(self.line_edit)

        self.combo_box = QComboBox(Widget)
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.setObjectName(u"combo_box")

        self.verticalLayout_2.addWidget(self.combo_box)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.button_2 = QPushButton(Widget)
        self.button_2.setObjectName(u"button_2")

        self.verticalLayout_3.addWidget(self.button_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.button_1.setText(QCoreApplication.translate("Widget", u"Button 1", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"GroupBox", None))
        self.radio_button_1.setText(QCoreApplication.translate("Widget", u"RadioButton", None))
        self.radio_button_2.setText(QCoreApplication.translate("Widget", u"RadioButton", None))
        self.radio_button_3.setText(QCoreApplication.translate("Widget", u"RadioButton", None))
        self.combo_box.setItemText(0, QCoreApplication.translate("Widget", u"Eins", None))
        self.combo_box.setItemText(1, QCoreApplication.translate("Widget", u"Zwei", None))
        self.combo_box.setItemText(2, QCoreApplication.translate("Widget", u"Drei", None))
        self.combo_box.setItemText(3, QCoreApplication.translate("Widget", u"Vier", None))
        self.combo_box.setItemText(4, QCoreApplication.translate("Widget", u"F\u00fcnf", None))

        self.button_2.setText(QCoreApplication.translate("Widget", u"Button 2", None))
    # retranslateUi

