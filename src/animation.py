import random

from PySide6.QtCore import QTimer, QRectF, Qt
from PySide6.QtGui import QPainter, QBrush, QPixmap
from PySide6.QtWidgets import QWidget

from src.objects.ball import Ball


class AnimationWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.balls = []
        self.pattern = "Обычный"
        self.background_path = ""
        self.background = None
        self.timer = QTimer(self)
        self.timer.setInterval(16)
        self.timer.timeout.connect(self.step)

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def set_pattern(self, pattern):
        self.pattern = pattern

    def set_background(self, path):
        self.background_path = path
        if path:
            self.background = QPixmap(path)
        else:
            self.background = None
        self.update()

    def set_balls(self, balls):
        self.balls = balls
        self.update()

    def randomize_balls(self, count, radius, speed):
        self.balls = []
        w = max(1, self.width())
        h = max(1, self.height())
        for _ in range(count):
            x = random.randint(radius, max(radius, w - radius))
            y = random.randint(radius, max(radius, h - radius))
            dx = random.uniform(-speed, speed)
            dy = random.uniform(-speed, speed)
            if dx == 0 and dy == 0:
                dx = speed
            color = random.choice(["red", "green", "blue", "yellow", "magenta", "cyan", "white"])
            self.balls.append(Ball(x, y, radius, dx, dy, color))
        self.update()

    def step(self):
        if not self.balls:
            return
        w = self.width()
        h = self.height()
        for ball in self.balls:
            if self.pattern == "Медленный":
                k = 0.5
            elif self.pattern == "Быстрый":
                k = 1.5
            elif self.pattern == "Прыгающий":
                k = 1.0
                ball.dy += 0.1
            else:
                k = 1.0
            ball.x += ball.dx * k
            ball.y += ball.dy * k
            if ball.x - ball.radius < 0:
                ball.x = ball.radius
                ball.dx = -ball.dx
            if ball.x + ball.radius > w:
                ball.x = w - ball.radius
                ball.dx = -ball.dx
            if ball.y - ball.radius < 0:
                ball.y = ball.radius
                ball.dy = -ball.dy
            if ball.y + ball.radius > h:
                ball.y = h - ball.radius
                ball.dy = -abs(ball.dy)
        n = len(self.balls)
        for i in range(n):
            for j in range(i + 1, n):
                b1 = self.balls[i]
                b2 = self.balls[j]
                dx = b2.x - b1.x
                dy = b2.y - b1.y
                dist2 = dx * dx + dy * dy
                min_dist = b1.radius + b2.radius
                if dist2 <= min_dist * min_dist and dist2 > 0:
                    b1.dx, b2.dx = b2.dx, b1.dx
                    b1.dy, b2.dy = b2.dy, b1.dy
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = QRectF(0, 0, self.width(), self.height())
        if self.background:
            painter.drawPixmap(rect.toRect(), self.background)
        else:
            painter.fillRect(rect, QBrush(self.palette().window().color()))
        for ball in self.balls:
            painter.setBrush(QBrush(ball.color))
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(ball.x - ball.radius, ball.y - ball.radius, ball.radius * 2, ball.radius * 2)

