from PySide6.QtWidgets import QWidget

from ui.ui_settings import Ui_Settings


class Settings(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
