import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_main_window import Ui_MainWindow # pyside6-uic ui/main_window.ui -o ui/ui_main_window.py

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())