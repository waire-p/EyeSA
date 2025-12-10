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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QFormLayout,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(514, 466)
        Settings.setStyleSheet(u"QWidget{\n"
"font: 16pt \"Bahnschrift\";\n"
"background-color: rgb(239, 255, 239);\n"
"color: rgb(40, 70, 40);\n"
"}\n"
"QPushButton{\n"
"border-radius: 10px;\n"
"transition: .2s linear;\n"
"background-color: rgb(209, 250, 209);\n"
"padding:5px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"min-width: 140px;\n"
"}\n"
"QSpinBox{\n"
"background-color: rgb(219, 255, 219);}\n"
"QCheckBox{\n"
"background-color: None;\n"
"accent-color:rgb(112, 148, 112);\n"
"font: 10pt \"Bahnschrift\";\n"
"}\n"
"QRadioButton{\n"
"background-color: None;\n"
"accent-color:rgb(112, 148, 112);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(Settings)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Settings)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(Settings)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_5 = QLabel(Settings)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_8 = QLabel(Settings)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_3 = QLabel(Settings)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_7 = QLabel(Settings)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.text = QRadioButton(Settings)
        self.break_mode = QButtonGroup(Settings)
        self.break_mode.setObjectName(u"break_mode")
        self.break_mode.addButton(self.text)
        self.text.setObjectName(u"text_2")
        self.text.setStyleSheet(u"")
        self.text.setChecked(True)

        self.verticalLayout_2.addWidget(self.text)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)

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
        self.timer_minutes.setMinimum(0)
        self.timer_minutes.setMaximum(59)
        self.timer_minutes.setValue(30)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.timer_minutes)

        self.timer_hours = QSpinBox(Settings)
        self.timer_hours.setObjectName(u"timer_hours")
        self.timer_hours.setMaximum(23)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.timer_hours)


        self.gridLayout.addLayout(self.formLayout, 0, 1, 1, 1)

        self.break_skip = QCheckBox(Settings)
        self.break_skip.setObjectName(u"break_skip")

        self.gridLayout.addWidget(self.break_skip, 3, 1, 1, 1)

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
        self.break_minutes.setMinimum(0)
        self.break_minutes.setMaximum(59)
        self.break_minutes.setValue(5)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.break_minutes)


        self.gridLayout.addLayout(self.formLayout_2, 4, 1, 1, 1)

        self.keyboard_lock = QCheckBox(Settings)
        self.keyboard_lock.setObjectName(u"keyboard_lock")
        self.keyboard_lock.setStyleSheet(u"")

        self.gridLayout.addWidget(self.keyboard_lock, 2, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.save_button = QPushButton(Settings)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.save_button)

        self.reset_button = QPushButton(Settings)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.reset_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)

        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label.setText(QCoreApplication.translate("Settings", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_4.setText(QCoreApplication.translate("Settings", u"\u0411\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u043a\u0430 \u043a\u043b\u0430\u0432\u0438\u0430\u0442\u0443\u0440\u044b", None))
        self.label_5.setText(QCoreApplication.translate("Settings", u"\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u043f\u0440\u043e\u043f\u0443\u0441\u043a\u0430\u0442\u044c \u043f\u0435\u0440\u0435\u0440\u044b\u0432\u044b", None))
        self.label_8.setText(QCoreApplication.translate("Settings", u"\u0412\u0440\u0435\u043c\u044f \u0442\u0430\u0439\u043c\u0435\u0440\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Settings", u"\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430 \u043f\u0440\u0438 \u043f\u0435\u0440\u0435\u0440\u044b\u0432\u0430\u0445", None))
        self.label_7.setText(QCoreApplication.translate("Settings", u"\u0412\u0440\u0435\u043c\u044f \u043f\u0435\u0440\u0435\u0440\u044b\u0432\u0430", None))
        self.text.setText(QCoreApplication.translate("Settings", u"\u0422\u0435\u043a\u0441\u0442", None))
        self.label_9.setText(QCoreApplication.translate("Settings", u"\u0421\u0435\u043a\u0443\u043d\u0434\u044b", None))
        self.label_10.setText(QCoreApplication.translate("Settings", u"\u041c\u0438\u043d\u0443\u0442\u044b", None))
        self.label_11.setText(QCoreApplication.translate("Settings", u"\u0427\u0430\u0441\u044b", None))
        self.break_skip.setText("")
        self.label_12.setText(QCoreApplication.translate("Settings", u"\u0421\u0435\u043a\u0443\u043d\u0434\u044b", None))
        self.label_13.setText(QCoreApplication.translate("Settings", u"\u041c\u0438\u043d\u0443\u0442\u044b", None))
        self.keyboard_lock.setText("")
        self.save_button.setText(QCoreApplication.translate("Settings", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.reset_button.setText(QCoreApplication.translate("Settings", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
    # retranslateUi

