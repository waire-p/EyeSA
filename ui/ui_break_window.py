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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_BreakWindow(object):
    def setupUi(self, BreakWindow):
        if not BreakWindow.objectName():
            BreakWindow.setObjectName(u"BreakWindow")
        BreakWindow.resize(492, 449)
        self.label = QLabel(BreakWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 170, 121, 151))

        self.retranslateUi(BreakWindow)

        QMetaObject.connectSlotsByName(BreakWindow)
    # setupUi

    def retranslateUi(self, BreakWindow):
        BreakWindow.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("BreakWindow", u"\u041e\u043a\u043e\u0448\u043a\u043e \u043f\u0435\u0440\u0435\u0440\u044b\u0432\u0430", None))
    # retranslateUi

