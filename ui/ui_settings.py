# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(462, 497)
        self.verticalLayout_3 = QVBoxLayout(Settings)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Settings)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_8 = QLabel(Settings)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_3 = QLabel(Settings)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(Settings)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_7 = QLabel(Settings)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)

        self.label_5 = QLabel(Settings)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_2 = QLabel(Settings)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.static_image = QRadioButton(Settings)
        self.static_image.setObjectName(u"static_image")

        self.verticalLayout_2.addWidget(self.static_image)

        self.video = QRadioButton(Settings)
        self.video.setObjectName(u"video")

        self.verticalLayout_2.addWidget(self.video)


        self.gridLayout.addLayout(self.verticalLayout_2, 2, 1, 1, 1)

        self.pushButton = QPushButton(Settings)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_9 = QLabel(Settings)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.label_10 = QLabel(Settings)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.label_11 = QLabel(Settings)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_11)

        self.timer_seconds = QSpinBox(Settings)
        self.timer_seconds.setObjectName(u"timer_seconds")
        self.timer_seconds.setAutoFillBackground(False)
        self.timer_seconds.setMaximum(59)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.timer_seconds)

        self.timer_minutes = QSpinBox(Settings)
        self.timer_minutes.setObjectName(u"timer_minutes")
        self.timer_minutes.setMaximum(59)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.timer_minutes)

        self.timer_hours = QSpinBox(Settings)
        self.timer_hours.setObjectName(u"timer_hours")
        self.timer_hours.setMaximum(23)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.timer_hours)


        self.gridLayout.addLayout(self.formLayout, 0, 1, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_12 = QLabel(Settings)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_12)

        self.label_13 = QLabel(Settings)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_13)

        self.break_seconds = QSpinBox(Settings)
        self.break_seconds.setObjectName(u"break_seconds")
        self.break_seconds.setMaximum(59)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.break_seconds)

        self.break_minutes = QSpinBox(Settings)
        self.break_minutes.setObjectName(u"break_minutes")
        self.break_minutes.setMaximum(59)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.break_minutes)


        self.gridLayout.addLayout(self.formLayout_2, 5, 1, 1, 1)

        self.checkBox_2 = QCheckBox(Settings)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 4, 1, 1, 1)

        self.checkBox = QCheckBox(Settings)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 3, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 2)

        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.save = QPushButton(Settings)
        self.save.setObjectName(u"save")

        self.horizontalLayout.addWidget(self.save)

        self.reset = QPushButton(Settings)
        self.reset.setObjectName(u"reset")

        self.horizontalLayout.addWidget(self.reset)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)

        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Form", None))
        self.label.setText(QCoreApplication.translate("Settings", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_8.setText(QCoreApplication.translate("Settings", u"\u0412\u0440\u0435\u043c\u044f \u0442\u0430\u0439\u043c\u0435\u0440\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Settings", u"\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430 \u043f\u0440\u0438 \u043f\u0435\u0440\u0435\u0440\u044b\u0432\u0430\u0445", None))
        self.label_4.setText(QCoreApplication.translate("Settings", u"\u041f\u043e\u043b\u043d\u0430\u044f \u0431\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u043a\u0430 \u044d\u043a\u0440\u0430\u043d\u0430", None))
        self.label_7.setText(QCoreApplication.translate("Settings", u"\u0412\u0440\u0435\u043c\u044f \u043f\u0435\u0440\u0435\u0440\u044b\u0432\u0430", None))
        self.label_5.setText(QCoreApplication.translate("Settings", u"\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u043f\u0440\u043e\u043f\u0443\u0441\u043a\u0430\u0442\u044c \u043f\u0435\u0440\u0435\u0440\u044b\u0432\u044b", None))
        self.label_2.setText(QCoreApplication.translate("Settings", u"TextLabel", None))
        self.static_image.setText(QCoreApplication.translate("Settings", u"\u0421\u0442\u0430\u0442\u0438\u0447\u043d\u0430\u044f", None))
        self.video.setText(QCoreApplication.translate("Settings", u"\u0412\u0438\u0434\u0435\u043e", None))
        self.pushButton.setText(QCoreApplication.translate("Settings", u"PushButton", None))
        self.label_9.setText(QCoreApplication.translate("Settings", u"\u0421\u0435\u043a\u0443\u043d\u0434\u044b", None))
        self.label_10.setText(QCoreApplication.translate("Settings", u"\u041c\u0438\u043d\u0443\u0442\u044b", None))
        self.label_11.setText(QCoreApplication.translate("Settings", u"\u0427\u0430\u0441\u044b", None))
        self.label_12.setText(QCoreApplication.translate("Settings", u"\u0421\u0435\u043a\u0443\u043d\u0434\u044b", None))
        self.label_13.setText(QCoreApplication.translate("Settings", u"\u041c\u0438\u043d\u0443\u0442\u044b", None))
        self.checkBox_2.setText("")
        self.checkBox.setText("")
        self.save.setText(QCoreApplication.translate("Settings", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.reset.setText(QCoreApplication.translate("Settings", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
    # retranslateUi

