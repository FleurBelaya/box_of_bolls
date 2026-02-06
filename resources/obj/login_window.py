from PySide6.QtWidgets import QMainWindow, QMessageBox

from ui.py.main_window import Ui_LoginWindow


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self._connect_signals()
        self._init_state()

    def _connect_signals(self):
        self.ui.new_btn.clicked.connect(self.on_create_project)
        self.ui.open_btn.clicked.connect(self.on_open_project)
        self.ui.exit_btn.clicked.connect(self.close)
        self.ui.project_list.itemDoubleClicked.connect(self.on_project_double_click)

    def _init_state(self):
        self.load_projects()
        self.ui.open_btn.setEnabled(False)

    def load_projects(self):
        self.ui.project_list.clear()
        # TODO: загрузка проектов из файловой системы
        # пример:
        # self.ui.project_list.addItem("Demo project")

    def on_create_project(self):
        # TODO: логика создания нового проекта
        QMessageBox.information(self, "Создание проекта", "Создать новый проект")

    def on_open_project(self):
        project = self.ui.project_list.currentItem()
        if not project:
            return
        self.open_project(project.text())

    def on_project_double_click(self, item):
        self.open_project(item.text())

    def open_project(self, project_name):
        # TODO: переход в окно редактора
        QMessageBox.information(self, "Открытие проекта", project_name)
