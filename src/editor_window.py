from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog,
    QColorDialog,
    QSpinBox,
    QDoubleSpinBox,
    QComboBox,
    QSlider,
    QMessageBox,
)
from PySide6.QtGui import QColor

from src.animation import AnimationWidget
from src.objects.ball import Ball
from src import project_manager


class EditorWindow(QMainWindow):
    project_saved = Signal(str)

    def __init__(self, project_name, project_data, parent=None):
        super().__init__(parent)
        self.project_name = project_name
        self.project_data = project_data or project_manager.create_default_project()
        self.current_color = QColor("red")
        self.setWindowTitle("Редактор заставки - " + self.project_name)
        self.resize(1000, 600)
        self.init_ui()
        self.load_from_data()

    def init_ui(self):
        central = QWidget(self)
        self.setCentralWidget(central)

        main_layout = QHBoxLayout(central)

        left = QVBoxLayout()
        main_layout.addLayout(left, 0)

        self.bg_label = QLabel("Фон:")
        left.addWidget(self.bg_label)

        self.bg_path_label = QLabel("Не выбран")
        left.addWidget(self.bg_path_label)

        self.bg_btn = QPushButton("Выбрать фон")
        self.bg_btn.clicked.connect(self.choose_background)
        left.addWidget(self.bg_btn)

        self.color_label = QLabel("Цвет шаров:")
        left.addWidget(self.color_label)

        self.color_btn = QPushButton("Выбрать цвет")
        self.color_btn.clicked.connect(self.choose_color)
        left.addWidget(self.color_btn)

        self.size_label = QLabel("Размер шара:")
        left.addWidget(self.size_label)

        self.size_spin = QSpinBox()
        self.size_spin.setRange(5, 200)
        self.size_spin.setValue(40)
        left.addWidget(self.size_spin)

        self.speed_label = QLabel("Скорость:")
        left.addWidget(self.speed_label)

        self.speed_spin = QDoubleSpinBox()
        self.speed_spin.setRange(0.1, 20.0)
        self.speed_spin.setSingleStep(0.1)
        self.speed_spin.setValue(5.0)
        left.addWidget(self.speed_spin)

        self.count_label = QLabel("Количество шаров:")
        left.addWidget(self.count_label)

        self.count_spin = QSpinBox()
        self.count_spin.setRange(1, 200)
        self.count_spin.setValue(10)
        left.addWidget(self.count_spin)

        self.pattern_label = QLabel("Общий паттерн поведения:")
        left.addWidget(self.pattern_label)

        self.pattern_box = QComboBox()
        self.pattern_box.addItems(["Обычный", "Медленный", "Быстрый", "Прыгающий"])
        self.pattern_box.currentTextChanged.connect(self.on_pattern_changed)
        left.addWidget(self.pattern_box)

        self.random_btn = QPushButton("Создать случайные шары")
        self.random_btn.clicked.connect(self.create_random_balls)
        left.addWidget(self.random_btn)

        self.add_btn = QPushButton("Добавить один шар")
        self.add_btn.clicked.connect(self.add_one_ball)
        left.addWidget(self.add_btn)

        self.clear_btn = QPushButton("Очистить сцену")
        self.clear_btn.clicked.connect(self.clear_balls)
        left.addWidget(self.clear_btn)

        left.addStretch()

        self.save_btn = QPushButton("Сохранить проект")
        self.save_btn.clicked.connect(self.save_project)
        left.addWidget(self.save_btn)

        self.preview_btn = QPushButton("Запустить/остановить предпросмотр")
        self.preview_btn.clicked.connect(self.toggle_preview)
        left.addWidget(self.preview_btn)

        self.fullscreen_btn = QPushButton("Запустить как заставку")
        self.fullscreen_btn.clicked.connect(self.run_fullscreen)
        left.addWidget(self.fullscreen_btn)

        right = QVBoxLayout()
        main_layout.addLayout(right, 1)

        self.preview_label = QLabel("Предпросмотр:")
        right.addWidget(self.preview_label)

        self.animation = AnimationWidget(self)
        right.addWidget(self.animation)

    def load_from_data(self):
        bg = self.project_data.get("background", "")
        pattern = self.project_data.get("pattern", "Обычный")
        balls_data = self.project_data.get("balls", [])

        if bg:
            self.bg_path_label.setText(bg)
            self.animation.set_background(bg)

        if pattern in ["Обычный", "Медленный", "Быстрый", "Прыгающий"]:
            self.pattern_box.setCurrentText(pattern)
            self.animation.set_pattern(pattern)

        balls = []
        for b in balls_data:
            x = b.get("x", 50)
            y = b.get("y", 50)
            r = b.get("radius", 40)
            dx = b.get("dx", 3)
            dy = b.get("dy", 3)
            color = b.get("color", "#ff0000")
            balls.append(Ball(x, y, r, dx, dy, color))
        self.animation.set_balls(balls)
        if balls:
            self.size_spin.setValue(int(balls[0].radius))
            self.speed_spin.setValue(float((abs(balls[0].dx) + abs(balls[0].dy)) / 2.0))

    def choose_background(self):
        path, _ = QFileDialog.getOpenFileName(self, "Выбор фона", "", "Изображения (*.png *.jpg *.jpeg *.bmp)")
        if not path:
            return
        self.bg_path_label.setText(path)
        self.animation.set_background(path)

    def choose_color(self):
        color = QColorDialog.getColor(self.current_color, self, "Выбор цвета шара")
        if not color.isValid():
            return
        self.current_color = color
        self.color_btn.setStyleSheet("background-color: %s" % color.name())

    def create_random_balls(self):
        count = self.count_spin.value()
        radius = self.size_spin.value()
        speed = self.speed_spin.value()
        self.animation.randomize_balls(count, radius, speed)

    def add_one_ball(self):
        radius = self.size_spin.value()
        speed = self.speed_spin.value()
        w = max(1, self.animation.width())
        h = max(1, self.animation.height())
        x = w // 2
        y = h // 2
        dx = speed
        dy = speed
        ball = Ball(x, y, radius, dx, dy, self.current_color)
        balls = list(self.animation.balls)
        balls.append(ball)
        self.animation.set_balls(balls)

    def clear_balls(self):
        self.animation.set_balls([])

    def on_pattern_changed(self, text):
        self.animation.set_pattern(text)

    def toggle_preview(self):
        if self.animation.timer.isActive():
            self.animation.stop()
        else:
            self.animation.start()

    def collect_data(self):
        data = {
            "background": self.bg_path_label.text() if self.bg_path_label.text() != "Не выбран" else "",
            "pattern": self.pattern_box.currentText(),
            "balls": []
        }
        for b in self.animation.balls:
            data["balls"].append(
                {
                    "x": b.x,
                    "y": b.y,
                    "radius": b.radius,
                    "dx": b.dx,
                    "dy": b.dy,
                    "color": b.color.name(),
                }
            )
        return data

    def save_project(self):
        data = self.collect_data()
        try:
            project_manager.save_project(self.project_name, data)
            QMessageBox.information(self, "Готово", "Проект сохранён.")
            self.project_saved.emit(self.project_name)
        except Exception:
            QMessageBox.warning(self, "Ошибка", "Не удалось сохранить проект.")

    def run_fullscreen(self):
        data = self.collect_data()
        self.fullscreen_window = FullscreenWindow(data, self)
        self.fullscreen_window.showFullScreen()
        self.fullscreen_window.start()


class FullscreenWindow(QMainWindow):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Заставка")
        self.animation = AnimationWidget(self)
        self.setCentralWidget(self.animation)
        bg = data.get("background", "")
        if bg:
            self.animation.set_background(bg)
        pattern = data.get("pattern", "Обычный")
        self.animation.set_pattern(pattern)
        balls = []
        for b in data.get("balls", []):
            x = b.get("x", 50)
            y = b.get("y", 50)
            r = b.get("radius", 40)
            dx = b.get("dx", 3)
            dy = b.get("dy", 3)
            color = b.get("color", "#ff0000")
            balls.append(Ball(x, y, r, dx, dy, color))
        if not balls:
            radius = 40
            dx = 5
            dy = 5
            balls.append(Ball(200, 200, radius, dx, dy, "#ff0000"))
        self.animation.set_balls(balls)

    def start(self):
        self.animation.start()

