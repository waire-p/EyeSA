from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTimer


from ui.ui_main_window import Ui_MainWindow
from data.settings_widget import Settings  # pyside6-uic ui/settings.ui -o ui/ui_settings.py
from data.about_widget import About  # pyside6-uic ui/about.ui -o ui/ui_about.py
from data.settings_reader import read_settings


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.start_button.clicked.connect(self.start)
        self.ui.settings_button.clicked.connect(self.open_settings)
        self.ui.about_button.clicked.connect(self.open_about)
        self.timer = QTimer()
        self.timer.timeout.connect(self.time_out)

        self.about = About()
        self.settings = Settings()

    def start(self):
        if self.ui.start_button.text() == 'Старт':
            self.ui.start_button.setText('Стоп')
            self.timer.start(read_settings()['timer'])
        else:
            self.ui.start_button.setText('Старт')
            self.timer.stop()

    def open_settings(self):
        self.timer.stop()
        self.ui.start_button.setText('Старт')
        self.settings.show()

    def open_about(self):
        self.about.show()

    def time_out(self):
        print(1)
