from PySide6.QtWidgets import QMainWindow, QMessageBox, QInputDialog
from PySide6.QtCore import Qt

from ui.login_ui import Ui_LoginWindow
from src.editor_window import EditorWindow
from src import project_manager


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.new_btn.clicked.connect(self.create_project)
        self.ui.open_btn.clicked.connect(self.open_project)
        self.ui.exit_btn.clicked.connect(self.close)
        self.ui.project_list.itemDoubleClicked.connect(self.open_selected_project)
        self.load_projects()

    def load_projects(self):
        self.ui.project_list.clear()
        names = project_manager.list_projects()
        for name in names:
            self.ui.project_list.addItem(name)

    def create_project(self):
        name, ok = QInputDialog.getText(self, "Новый проект", "Введите имя проекта:")
        if not ok:
            return
        name = name.strip()
        if not name:
            QMessageBox.warning(self, "Ошибка", "Имя проекта не может быть пустым.")
            return
        if name in project_manager.list_projects():
            QMessageBox.warning(self, "Ошибка", "Проект с таким именем уже существует.")
            return
        data = project_manager.create_default_project()
        project_manager.save_project(name, data)
        self.load_projects()
        self.open_editor(name, data)

    def open_project(self):
        item = self.ui.project_list.currentItem()
        if not item:
            QMessageBox.warning(self, "Ошибка", "Выберите проект в списке.")
            return
        name = item.text()
        data = project_manager.load_project(name)
        if data is None:
            QMessageBox.warning(self, "Ошибка", "Не удалось загрузить проект.")
            return
        self.open_editor(name, data)

    def open_selected_project(self, item):
        if not item:
            return
        name = item.text()
        data = project_manager.load_project(name)
        if data is None:
            QMessageBox.warning(self, "Ошибка", "Не удалось загрузить проект.")
            return
        self.open_editor(name, data)

    def open_editor(self, name, data):
        self.editor = EditorWindow(project_name=name, project_data=data, parent=self)
        self.editor.project_saved.connect(self.on_project_saved)
        self.editor.show()
        self.hide()

    def on_project_saved(self, name):
        self.load_projects()
        self.show()

