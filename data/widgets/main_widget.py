from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTimer

from data.ui.ui_main_window import Ui_MainWindow
from data.widgets.settings_widget import Settings  # pyside6-uic ui/settings.ui -o ui/ui_settings.py
from data.widgets.about_widget import About  # pyside6-uic ui/about.ui -o ui/ui_about.py
from data.widgets.break_widget import BreakWindow  # pyside6-uic ui/break_window.ui -o ui/ui_break_window.py
from data.widgets.notification_dialog import BreakNotification  # pyside6-uic ui/break_notification.ui -o ui/ui_notification_dialog.py
from data.modules.settings_reader import read_settings


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.start_button.clicked.connect(self.start)
        self.ui.settings_button.clicked.connect(self.open_settings)
        self.ui.about_button.clicked.connect(self.open_about)
        self.timer = QTimer(singleShot=True)  # Таймер между перерывами
        self.break_timer = QTimer(singleShot=True)  # Таймер перерывов
        self.notification_timer = QTimer(singleShot=True)
        self.timer.timeout.connect(self.timer_timeout)
        self.break_timer.timeout.connect(self.break_timer_timeout)
        self.notification_timer.timeout.connect(self.show_notification)

        self.about = About()
        self.settings = Settings()
        self.break_window = BreakWindow()
        self.dialog = BreakNotification()

    def start(self):
        if self.ui.start_button.text() == 'Старт':
            self.ui.start_button.setText('Стоп')
            self.timer.start(read_settings()['timer'])
            self.notification_timer.start(read_settings()['timer'] * 3 // 4)
        else:
            self.ui.start_button.setText('Старт')
            self.timer.stop()
            self.break_timer.stop()
            self.notification_timer.stop()

    def open_settings(self):
        self.timer.stop()
        self.ui.start_button.setText('Старт')
        self.settings.change_values()
        self.settings.show()

    def open_about(self):
        self.about.show()

    def timer_timeout(self):
        self.break_timer.start(read_settings()['break_time'])
        self.break_window.is_skippable()
        if read_settings()['mode'] == 'text':
            self.break_window.set_text_mode()
        self.dialog.close()
        self.break_window.showFullScreen()
        self.break_window.block()

    def break_timer_timeout(self):
        self.break_timer.stop()
        self.break_window.unblock()
        self.notification_timer.start(read_settings()['timer'] * 3 // 4)
        self.break_window.hide()
        self.timer.start(read_settings()['timer'])

    def show_notification(self):
        self.dialog.update_text()
        f = self.dialog.skip()
        """if f:
            print('Skip!')
            self.timer.stop()
            self.break_timer.stop()
            self.notification_timer.start(read_settings()['timer'] * 3 // 4)
            self.timer.start(read_settings()['timer'])"""
        self.dialog.exec()
        f = False
        print('Напомнили!')
