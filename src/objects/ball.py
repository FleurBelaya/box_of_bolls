from PySide6.QtGui import QColor


class Ball:
    def __init__(self, x, y, radius, dx, dy, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.dx = dx
        self.dy = dy
        if isinstance(color, QColor):
            self.color = color
        else:
            self.color = QColor(color)

