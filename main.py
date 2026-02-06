import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BALLS_PATH = os.path.join(BASE_DIR, "resources", "balls.png")

from PySide6.QtWidgets import QApplication
from resources.obj import LoginWindow

app = QApplication(sys.argv)
window = LoginWindow()
window.show()
sys.exit(app.exec())
