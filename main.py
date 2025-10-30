import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from ui.ui_main_window import Ui_MainWindow # pyside6-uic ui/main_window.ui -o ui/ui_main_window.py
from ui.ui_about import Ui_About # pyside6-uic ui/about.ui -o ui/ui_about.py
from datetime import time


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.start_button.clicked.connect(self.start)
        #self.ui.settings_button.clicked.connect(self.open_settings)
        self.ui.about_button.clicked.connect(self.open_about)

    def start(self):
        if self.ui.start_button.text() == 'Старт':
            self.ui.start_button.setText('Стоп')
        else:
            self.ui.start_button.setText('Старт')

    def open_settings(self):
        pass

    def open_about(self):
        about = About()
        about.show()

class About(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_About()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())