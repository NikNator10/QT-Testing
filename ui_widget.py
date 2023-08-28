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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(252, 385)
        self.verticalLayout_4 = QVBoxLayout(Widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.button_1 = QPushButton(Widget)
        self.button_1.setObjectName(u"button_1")

        self.verticalLayout_4.addWidget(self.button_1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.group_box = QGroupBox(Widget)
        self.group_box.setObjectName(u"group_box")
        self.verticalLayout = QVBoxLayout(self.group_box)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkbox_1 = QCheckBox(self.group_box)
        self.checkbox_1.setObjectName(u"checkbox_1")

        self.verticalLayout.addWidget(self.checkbox_1)

        self.checkbox_2 = QCheckBox(self.group_box)
        self.checkbox_2.setObjectName(u"checkbox_2")

        self.verticalLayout.addWidget(self.checkbox_2)

        self.checkbox_3 = QCheckBox(self.group_box)
        self.checkbox_3.setObjectName(u"checkbox_3")

        self.verticalLayout.addWidget(self.checkbox_3)


        self.horizontalLayout.addWidget(self.group_box)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.combo_box = QComboBox(Widget)
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.setObjectName(u"combo_box")

        self.verticalLayout_2.addWidget(self.combo_box)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.line_edit = QLineEdit(Widget)
        self.line_edit.setObjectName(u"line_edit")

        self.verticalLayout_4.addWidget(self.line_edit)

        self.button_2 = QPushButton(Widget)
        self.button_2.setObjectName(u"button_2")

        self.verticalLayout_4.addWidget(self.button_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_1 = QLabel(Widget)
        self.label_1.setObjectName(u"label_1")
        font = QFont()
        font.setPointSize(20)
        self.label_1.setFont(font)

        self.verticalLayout_3.addWidget(self.label_1)

        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_3.addWidget(self.label_4)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.button_1.setText(QCoreApplication.translate("Widget", u"Click here", None))
        self.group_box.setTitle(QCoreApplication.translate("Widget", u"GroupBox", None))
        self.checkbox_1.setText(QCoreApplication.translate("Widget", u"CheckBox", None))
        self.checkbox_2.setText(QCoreApplication.translate("Widget", u"CheckBox", None))
        self.checkbox_3.setText(QCoreApplication.translate("Widget", u"CheckBox", None))
        self.combo_box.setItemText(0, QCoreApplication.translate("Widget", u"Linux", None))
        self.combo_box.setItemText(1, QCoreApplication.translate("Widget", u"Windows", None))
        self.combo_box.setItemText(2, QCoreApplication.translate("Widget", u"MacOS", None))

        self.button_2.setText(QCoreApplication.translate("Widget", u"Click here", None))
        self.label_1.setText(QCoreApplication.translate("Widget", u"This", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"is", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"some", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"text", None))
    # retranslateUi

