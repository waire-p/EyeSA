from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTimer


from ui.ui_main_window import Ui_MainWindow
from data.settings_widget import Settings  # pyside6-uic ui/settings.ui -o ui/ui_settings.py
from data.about_widget import About  # pyside6-uic ui/about.ui -o ui/ui_about.py
from data.break_widget import BreakWindow  # pyside6-uic ui/break_window.ui -o ui/ui_break_window.py
from data.settings_reader import read_settings


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.start_button.clicked.connect(self.start)
        self.ui.settings_button.clicked.connect(self.open_settings)
        self.ui.about_button.clicked.connect(self.open_about)
        self.timer = QTimer() # Таймер между перерывами
        self.break_timer = QTimer() # Таймер перерывов
        self.timer.timeout.connect(self.timer_timeout)
        self.break_timer.timeout.connect(self.break_timer_timeout)

        self.about = About()
        self.settings = Settings()
        self.break_window = BreakWindow()

    def start(self):
        if self.ui.start_button.text() == 'Старт':
            self.ui.start_button.setText('Стоп')
            self.timer.start(read_settings()['timer'])
        else:
            self.ui.start_button.setText('Старт')
            self.timer.stop()
            self.break_timer.stop()

    def open_settings(self):
        self.timer.stop()
        self.ui.start_button.setText('Старт')
        self.settings.show()
        self.settings.change_values()

    def open_about(self):
        self.about.show()

    def timer_timeout(self):
        self.timer.stop()
        self.break_timer.start(read_settings()['break_time'])
        self.break_window.is_skippable()
        self.break_window.show()

    def break_timer_timeout(self):
        self.break_timer.stop()
        self.break_window.hide()
        self.timer.start(read_settings()['timer'])
