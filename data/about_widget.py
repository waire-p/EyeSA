from PySide6.QtWidgets import QWidget

from ui.ui_about import Ui_About


class About(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_About()
        self.ui.setupUi(self)
