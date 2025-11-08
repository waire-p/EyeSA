from PySide6.QtWidgets import QDialog
from data.settings_reader import read_settings
from ui.ui_notification_dialog import Ui_BreakNotification
import pymorphy3


class BreakNotification(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_BreakNotification()
        self.ui.setupUi(self)

    def update_text(self):
        time_remaining = read_settings()['timer'] * 1 // 4
        hours = int(time_remaining / (1000 * 60 * 60)) % 24
        minutes = int(time_remaining / (1000 * 60)) % 60
        seconds = int(time_remaining / 1000) % 60
        message = 'До перерыва осталось: '
        morph = pymorphy3.MorphAnalyzer()
        if hours != 0:
            # переводим число в строку и склоняем слово 'час'
            hours = str(hours) + ' ' + morph.parse('час')[0].make_agree_with_number(hours).word + ' '
            message += hours
        if minutes != 0:
            # переводим число в строку и склоняем слово 'минута'
            minutes = str(minutes) + ' ' + morph.parse('минута')[0].make_agree_with_number(minutes).word + ' '
            message += minutes
        if seconds != 0:
            # переводим число в строку и склоняем слово 'секунда'
            seconds = str(seconds) + ' ' + morph.parse('секунда')[0].make_agree_with_number(seconds).word
            message += seconds
        self.ui.message.setText(message)
