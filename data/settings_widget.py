from PySide6.QtWidgets import QWidget

from ui.ui_settings import Ui_Settings
import json
from data.settings_reader import read_settings


class Settings(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        self.ui.save_button.clicked.connect(self.save_settings)
        self.ui.reset_button.clicked.connect(self.reset_settings)
        self.change_values()

    def save_settings(self):
        with open('data/settings.json', mode='w') as file:
            new_settings = {'keyboard_lock': self.ui.keyboard_lock.isChecked(),
                            'break_skip': self.ui.break_skip.isChecked(),
                            'mode': self.ui.break_mode.checkedButton().objectName()}
            hours, minutes, seconds = int(self.ui.timer_hours.text()), \
                int(self.ui.timer_minutes.text()), int(self.ui.timer_seconds.text())
            milliseconds = hours * 3600 * 1000 + minutes * 60 * 1000 + seconds * 1000
            if milliseconds < 60000:
                milliseconds = 60000
            new_settings['timer'] = milliseconds
            minutes, seconds = int(self.ui.break_minutes.text()), int(self.ui.break_seconds.text())
            milliseconds = minutes * 60 * 1000 + seconds * 1000
            if milliseconds <= 60000:
                milliseconds = 60000
            new_settings['break_time'] = milliseconds
            json.dump(new_settings, file)
        self.close()

    def reset_settings(self):
        with open('data/settings.json', mode='w') as file:
            new_settings = {'keyboard_lock': False,
                            'break_skip': False,
                            'mode': 'static_image',
                            'timer': 1800000,
                            'break_time': 300000}
            json.dump(new_settings, file)
        self.close()

    def change_values(self):
        settings = read_settings()
        self.ui.break_skip.setChecked(settings['break_skip'])
        self.ui.keyboard_lock.setChecked(settings['keyboard_lock'])
        if settings['mode'] == 'static_image':
            self.ui.static_image.setChecked(True)
        else:
            self.ui.video.setChecked(True)
        # перевод миллисекунд в часы, минуты и секунды
        self.ui.timer_hours.setValue(int(settings['timer'] / (1000 * 60 * 60)) % 24)
        self.ui.timer_minutes.setValue(int(settings['timer'] / (1000 * 60)) % 60)
        self.ui.timer_seconds.setValue(int(settings['timer'] / 1000) % 60)
        # перевод миллисекунд в минуты и секунды
        self.ui.break_minutes.setValue(int(settings['break_time'] / (1000 * 60)) % 60)
        self.ui.break_seconds.setValue((int(settings['break_time'] / 1000) % 60))
