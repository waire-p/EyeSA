# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'break_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_BreakWindow(object):
    def setupUi(self, BreakWindow):
        if not BreakWindow.objectName():
            BreakWindow.setObjectName(u"BreakWindow")
        BreakWindow.resize(301, 278)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BreakWindow.sizePolicy().hasHeightForWidth())
        BreakWindow.setSizePolicy(sizePolicy)
        BreakWindow.setStyleSheet(u"font: 16pt \"Bahnschrift\";\n"
"background-color: rgb(239, 255, 239);")
        self.verticalLayout = QVBoxLayout(BreakWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.skip_button = QPushButton(BreakWindow)
        self.skip_button.setObjectName(u"skip_button")
        self.skip_button.setStyleSheet(u"border-radius: 10px;\n"
"color: rgb(40, 70, 40);\n"
"transition: .2s linear;\n"
"background-color: rgb(209, 250, 209);\n"
"padding:5px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"")

        self.verticalLayout.addWidget(self.skip_button)

        self.label = QLabel(BreakWindow)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(BreakWindow)

        QMetaObject.connectSlotsByName(BreakWindow)
    # setupUi

    def retranslateUi(self, BreakWindow):
        BreakWindow.setWindowTitle("")
        self.skip_button.setText(QCoreApplication.translate("BreakWindow", u"\u041f\u0440\u043e\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        self.label.setText("")
    # retranslateUi

