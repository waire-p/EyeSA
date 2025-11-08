# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'break_notification.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_BreakNotification(object):
    def setupUi(self, BreakNotification):
        if not BreakNotification.objectName():
            BreakNotification.setObjectName(u"BreakNotification")
        BreakNotification.resize(310, 100)
        BreakNotification.setMinimumSize(QSize(310, 100))
        BreakNotification.setMaximumSize(QSize(310, 100))
        self.verticalLayout = QVBoxLayout(BreakNotification)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.message = QLabel(BreakNotification)
        self.message.setObjectName(u"message")
        self.message.setAcceptDrops(True)

        self.verticalLayout.addWidget(self.message)


        self.retranslateUi(BreakNotification)

        QMetaObject.connectSlotsByName(BreakNotification)
    # setupUi

    def retranslateUi(self, BreakNotification):
        BreakNotification.setWindowTitle(QCoreApplication.translate("BreakNotification", u"\u0412\u043d\u0438\u043c\u0430\u043d\u0438\u0435!", None))
        self.message.setText("")
    # retranslateUi

