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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_BreakNotification(object):
    def setupUi(self, BreakNotification):
        if not BreakNotification.objectName():
            BreakNotification.setObjectName(u"BreakNotification")
        BreakNotification.resize(310, 100)
        BreakNotification.setMinimumSize(QSize(310, 100))
        BreakNotification.setMaximumSize(QSize(310, 100))
        self.verticalLayout = QVBoxLayout(BreakNotification)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.message = QLabel(BreakNotification)
        self.message.setObjectName(u"message")
        self.message.setAcceptDrops(True)

        self.verticalLayout_2.addWidget(self.message)

        self.skip_btn = QPushButton(BreakNotification)
        self.skip_btn.setObjectName(u"skip_btn")

        self.verticalLayout_2.addWidget(self.skip_btn)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(BreakNotification)

        QMetaObject.connectSlotsByName(BreakNotification)
    # setupUi

    def retranslateUi(self, BreakNotification):
        BreakNotification.setWindowTitle(QCoreApplication.translate("BreakNotification", u"\u0412\u043d\u0438\u043c\u0430\u043d\u0438\u0435!", None))
        self.message.setText("")
        self.skip_btn.setText(QCoreApplication.translate("BreakNotification", u"\u041f\u0440\u043e\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
    # retranslateUi

