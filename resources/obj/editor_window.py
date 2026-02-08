import os

from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtWidgets import QMainWindow

from ui.py.ui_editor_window import Ui_MainWindow


class EditorWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._player = None
        self._audio_output = None
        self._current_music_path = ""
        self._setup_music_logic()

    def _setup_music_logic(self):
        if not hasattr(self.ui, "music_combo"):
            return
        self.ui.music_combo.clear()
        self.ui.music_combo.addItem("Без музыки", "")
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        music_dir = os.path.join(base_dir, "db", "music")
        if os.path.isdir(music_dir):
            for name in sorted(os.listdir(music_dir)):
                if not name.lower().endswith((".mp3", ".wav", ".ogg")):
                    continue
                full_path = os.path.join(music_dir, name)
                self.ui.music_combo.addItem(name, full_path)
        self._player = QMediaPlayer(self)
        self._audio_output = QAudioOutput(self)
        self._player.setAudioOutput(self._audio_output)
        self._audio_output.setVolume(0.5)
        self.ui.music_combo.currentIndexChanged.connect(self._on_music_changed)
        self._player.playbackStateChanged.connect(self._on_playback_state_changed)

    def _on_music_changed(self, index):
        if self._player is None:
            return
        path = self.ui.music_combo.itemData(index)
        self._current_music_path = path or ""
        if not self._current_music_path:
            self._player.stop()
            return
        url = QUrl.fromLocalFile(self._current_music_path)
        self._player.setSource(url)
        self._player.play()

    def _on_playback_state_changed(self, state):
        if self._player is None:
            return
        if not self._current_music_path:
            return
        if state == QMediaPlayer.PlaybackState.StoppedState:
            self._player.play()
