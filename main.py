import sys
from PySide6.QtWidgets import QApplication
from data.main_widget import MainWindow  # pyside6-uic ui/main_window.ui -o ui/ui_main_window.py

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
# Уведомления как диалоговые окна
# экран перерыва как отдельное окно
# посмотреть виджеты для картинок\видео\анимаций
