import sys
from PySide6.QtWidgets import QApplication
from data.widgets.main_widget import MainWindow  # pyside6-uic ui/main_window.ui -o ui/ui_main_window.py

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())

# посмотреть виджеты для картинок
# переименовать параметр screen_lock на клаву, попробовать сделать сочетания клавиш и начать дизайн