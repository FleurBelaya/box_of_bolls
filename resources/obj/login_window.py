from PySide6.QtWidgets import QMainWindow

from resources.obj.editor_window import EditorWindow
from ui.py.main_window import Ui_LoginWindow


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.ui.open_btn.setEnabled(False)
        self._connect_signals()

    def _connect_signals(self):
        self.ui.new_btn.clicked.connect(self.on_create_project)
        self.ui.exit_btn.clicked.connect(self.close)

    def on_create_project(self):
        self.open_editor()

    def open_editor(self):
        self.editor_window = EditorWindow(self)
        self.editor_window.show()
        self.hide()
