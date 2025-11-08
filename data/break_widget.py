from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from ui.ui_break_window import Ui_BreakWindow
from data.settings_reader import read_settings


class BreakWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_BreakWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Window | Qt.WindowMaximizeButtonHint)

    def is_skippable(self):
        if not read_settings()['break_skip']:
            pass

    def closeEvent(self, event):
        if not read_settings()['break_skip']:
            event.ignore()
        else:
            event.accept()
            self.is_closed = True
            super().closeEvent(event)


# делать через отдельную кнопку закрытие окна
