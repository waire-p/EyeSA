from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Qt, QTimer
from data.ui.ui_break_window import Ui_BreakWindow
from data.settings_reader import read_settings
import pyautogui
import keyboard


class BreakWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_BreakWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Window | Qt.WindowMaximizeButtonHint | Qt.WindowStaysOnTopHint)
        self.mouse_mover = QTimer()
        self.mouse_mover.timeout.connect(self.move_mouse)
        for screen in QApplication.screens():
            self.width, self.height = screen.size().width(), screen.size().height()


    def is_skippable(self):
        if not read_settings()['break_skip']:
            self.ui.skip_button.hide()

    def closeEvent(self, event):
        if not read_settings()['break_skip']:
            event.ignore()
        else:
            event.accept()
            self.is_closed = True
            super().closeEvent(event)

    def move_mouse(self):
        pyautogui.moveTo(self.width // 2, 35)

    def block_mouse(self):
        if read_settings()['break_skip']:
            for i in range(150):
                keyboard.block_key(i)
        self.mouse_mover.start(100)

    def unblock_mouse(self):
        if read_settings()['break_skip']:
            for i in range(150):
                keyboard.unblock_key(i)
        self.mouse_mover.stop()
