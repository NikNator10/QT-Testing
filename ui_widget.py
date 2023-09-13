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
from PySide6.QtWidgets import (QApplication, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(351, 579)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.list_widget = QListWidget(Widget)
        self.list_widget.setObjectName(u"list_widget")

        self.verticalLayout.addWidget(self.list_widget)

        self.horizontalSpacer = QSpacerItem(336, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.choose_dir_button = QPushButton(Widget)
        self.choose_dir_button.setObjectName(u"choose_dir_button")

        self.verticalLayout.addWidget(self.choose_dir_button)

        self.line_edit = QLineEdit(Widget)
        self.line_edit.setObjectName(u"line_edit")

        self.verticalLayout.addWidget(self.line_edit)

        self.horizontalSpacer_2 = QSpacerItem(336, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)

        self.create_dir_button = QPushButton(Widget)
        self.create_dir_button.setObjectName(u"create_dir_button")

        self.verticalLayout.addWidget(self.create_dir_button)

        self.delete_dir_button = QPushButton(Widget)
        self.delete_dir_button.setObjectName(u"delete_dir_button")

        self.verticalLayout.addWidget(self.delete_dir_button)

        self.dir_exists_button = QPushButton(Widget)
        self.dir_exists_button.setObjectName(u"dir_exists_button")

        self.verticalLayout.addWidget(self.dir_exists_button)

        self.folder_content_button = QPushButton(Widget)
        self.folder_content_button.setObjectName(u"folder_content_button")

        self.verticalLayout.addWidget(self.folder_content_button)

        self.dir_file_button = QPushButton(Widget)
        self.dir_file_button.setObjectName(u"dir_file_button")

        self.verticalLayout.addWidget(self.dir_file_button)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.choose_dir_button.setText(QCoreApplication.translate("Widget", u"Choose Dir", None))
        self.create_dir_button.setText(QCoreApplication.translate("Widget", u"Create Dir", None))
        self.delete_dir_button.setText(QCoreApplication.translate("Widget", u"Delete Dir", None))
        self.dir_exists_button.setText(QCoreApplication.translate("Widget", u"Dir Exist ?", None))
        self.folder_content_button.setText(QCoreApplication.translate("Widget", u"Folder Contents", None))
        self.dir_file_button.setText(QCoreApplication.translate("Widget", u"Dir or File?", None))
    # retranslateUi

