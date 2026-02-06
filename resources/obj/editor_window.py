from PySide6.QtWidgets import QMainWindow

from ui.py.editor_window import Ui_MainWindow


class EditorWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

