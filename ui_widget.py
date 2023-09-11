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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(440, 354)
        self.horizontalLayout_2 = QHBoxLayout(Widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.choose_dir_button = QPushButton(Widget)
        self.choose_dir_button.setObjectName(u"choose_dir_button")

        self.verticalLayout_2.addWidget(self.choose_dir_button)

        self.create_dir_button = QPushButton(Widget)
        self.create_dir_button.setObjectName(u"create_dir_button")

        self.verticalLayout_2.addWidget(self.create_dir_button)

        self.remove_dir_button = QPushButton(Widget)
        self.remove_dir_button.setObjectName(u"remove_dir_button")

        self.verticalLayout_2.addWidget(self.remove_dir_button)

        self.dir_exists_button = QPushButton(Widget)
        self.dir_exists_button.setObjectName(u"dir_exists_button")

        self.verticalLayout_2.addWidget(self.dir_exists_button)

        self.folder_content_button = QPushButton(Widget)
        self.folder_content_button.setObjectName(u"folder_content_button")

        self.verticalLayout_2.addWidget(self.folder_content_button)

        self.dir_file_button = QPushButton(Widget)
        self.dir_file_button.setObjectName(u"dir_file_button")

        self.verticalLayout_2.addWidget(self.dir_file_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.line_edit = QLineEdit(Widget)
        self.line_edit.setObjectName(u"line_edit")

        self.horizontalLayout.addWidget(self.line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.list_widget = QListWidget(Widget)
        self.list_widget.setObjectName(u"list_widget")

        self.verticalLayout.addWidget(self.list_widget)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.choose_dir_button.setText(QCoreApplication.translate("Widget", u"Choose Directory", None))
        self.create_dir_button.setText(QCoreApplication.translate("Widget", u"Create Directory", None))
        self.remove_dir_button.setText(QCoreApplication.translate("Widget", u"Delete Directory", None))
        self.dir_exists_button.setText(QCoreApplication.translate("Widget", u"Does Dir exist?", None))
        self.folder_content_button.setText(QCoreApplication.translate("Widget", u"List Folder Content", None))
        self.dir_file_button.setText(QCoreApplication.translate("Widget", u"Dir or file?", None))
    # retranslateUi

