# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_About(object):
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName(u"About")
        About.resize(240, 200)
        About.setAcceptDrops(True)
        About.setStyleSheet(u"QWidget{\n"
"font: 16pt \"Bahnschrift\";\n"
"background-color: rgb(239, 255, 239);\n"
"color: rgb(40, 70, 40);\n"
"}\n"
"QLabel{\n"
"min-width: 220px;\n"
"min-height:180px;}")
        self.horizontalLayout = QHBoxLayout(About)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(About)
        self.label.setObjectName(u"label")
        self.label.setAcceptDrops(False)
        self.label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label)


        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)
    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.label.setText(QCoreApplication.translate("About", u"\u042d\u0442\u043e \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0431\u044b\u043b\u043e \u0441\u043e\u0437\u0434\u0430\u043d\u043e \u0434\u043b\u044f \u043a\u043e\u043d\u0442\u0440\u043e\u043b\u044f \u0432\u0440\u0435\u043c\u0435\u043d\u0438, \u043f\u0440\u043e\u0432\u0435\u0434\u0451\u043d\u043d\u043e\u0433\u043e \u0437\u0430 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043e\u043c.\u0421\u043e\u0437\u0434\u0430\u043d\u043e \u0432 2025 \u0433\u043e\u0434\u0443", None))
    # retranslateUi

