from PySide6.QtWidgets import QWidget

from ui.ui_settings import Ui_Settings
import json

class Settings(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        self.ui.save_button.clicked.connect(self.save_settings)
        self.ui.reset_button.clicked.connect(self.reset_settings)
        with open('data/settings.json') as file:
            settings = json.load(file)
            print(settings)

    def save_settings(self):
        with open('data/settings.json', mode='w') as file:
            new_settings = {}
            new_settings['screen_lock'] = self.ui.screen_lock.isChecked()
            new_settings['break_skip'] = self.ui.break_skip.isChecked()
            new_settings['mode'] = self.ui.break_mode.checkedButton().objectName()
            hours, minutes, seconds = int(self.ui.timer_hours.text()), int(self.ui.timer_minutes.text()),\
                int(self.ui.timer_seconds.text())
            milliseconds = hours*3600*1000+minutes*60*1000+seconds*1000
            new_settings['timer'] = milliseconds
            minutes, seconds = int(self.ui.break_minutes.text()), int(self.ui.break_seconds.text())
            milliseconds = minutes * 60 * 1000 + seconds * 1000
            new_settings['break_time'] = milliseconds
            json.dump(new_settings)

    def reset_settings(self):
        with open('data/settings.json', mode='w') as file:
            new_settings = {'screen_lock': False,
                            'break_skip': False,
                            'mode': 'static_image',
                            'timer': 1800000,
                            'break_time': 300000}
            json.dump(new_settings)
