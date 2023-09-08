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
        Widget.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.dir_path_line_edit = QLineEdit(Widget)
        self.dir_path_line_edit.setObjectName(u"dir_path_line_edit")

        self.verticalLayout_2.addWidget(self.dir_path_line_edit)

        self.list_widget = QListWidget(Widget)
        self.list_widget.setObjectName(u"list_widget")

        self.verticalLayout_2.addWidget(self.list_widget)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.choose_dir_button = QPushButton(Widget)
        self.choose_dir_button.setObjectName(u"choose_dir_button")

        self.verticalLayout.addWidget(self.choose_dir_button)

        self.create_dir_button = QPushButton(Widget)
        self.create_dir_button.setObjectName(u"create_dir_button")

        self.verticalLayout.addWidget(self.create_dir_button)

        self.dir_exists_button = QPushButton(Widget)
        self.dir_exists_button.setObjectName(u"dir_exists_button")

        self.verticalLayout.addWidget(self.dir_exists_button)

        self.dir_or_file_button = QPushButton(Widget)
        self.dir_or_file_button.setObjectName(u"dir_or_file_button")

        self.verticalLayout.addWidget(self.dir_or_file_button)

        self.folder_content_button = QPushButton(Widget)
        self.folder_content_button.setObjectName(u"folder_content_button")

        self.verticalLayout.addWidget(self.folder_content_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.choose_dir_button.setText(QCoreApplication.translate("Widget", u"Choose Dir", None))
        self.create_dir_button.setText(QCoreApplication.translate("Widget", u"Create Dir", None))
        self.dir_exists_button.setText(QCoreApplication.translate("Widget", u"Dir exists?", None))
        self.dir_or_file_button.setText(QCoreApplication.translate("Widget", u"Dir or File", None))
        self.folder_content_button.setText(QCoreApplication.translate("Widget", u"Folder Contents", None))
    # retranslateUi

