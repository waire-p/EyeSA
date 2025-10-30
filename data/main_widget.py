from PySide6.QtWidgets import QMainWindow

from ui.ui_main_window import Ui_MainWindow
from data.settings_widget import Settings  # pyside6-uic ui/settings.ui -o ui/ui_settings.py
from data.about_widget import About  # pyside6-uic ui/about.ui -o ui/ui_about.py


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.start_button.clicked.connect(self.start)
        self.ui.settings_button.clicked.connect(self.open_settings)
        self.ui.about_button.clicked.connect(self.open_about)

        self.about = About()
        self.settings = Settings()

    def start(self):
        if self.ui.start_button.text() == 'Старт':
            self.ui.start_button.setText('Стоп')
        else:
            self.ui.start_button.setText('Старт')

    def open_settings(self):
        self.settings.show()

    def open_about(self):
        self.about.show()
