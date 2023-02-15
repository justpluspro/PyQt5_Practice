import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QSlider


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.player = QMediaPlayer(self)
        self.player.stateChanged.connect(self.media_play_state_changed)

    def init_ui(self):
        self.setWindowTitle('播放音乐')
        self.resize(400, 500)
        self.play_btn = QPushButton('播放')
        self.pause_btn = QPushButton('暂停')

        self.volumn_slider = QSlider()
        self.volumn_slider.setValue(50)
        self.volumn_slider.setTickInterval(10)
        self.volumn_slider.setRange(0, 100)
        self.volumn_slider.valueChanged.connect(self.volumn_slider_value_changed)

        self.play_btn.clicked.connect(self.play_music)
        self.pause_btn.clicked.connect(self.pause_music)

        self.tool_btn_layout = QHBoxLayout()
        self.tool_btn_layout.addWidget(self.play_btn)
        self.tool_btn_layout.addWidget(self.pause_btn)
        self.tool_btn_layout.addWidget(self.volumn_slider)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.tool_btn_layout)

        self.setLayout(self.main_layout)

    def play_music(self):
        print('play')
        self.file_path = '1.mp3'
        url = QUrl.fromLocalFile(self.file_path)
        self.media_content = QMediaContent(url)
        self.player.setMedia(self.media_content)
        self.player.setVolume(80)
        self.player.play()

    def pause_music(self):
        print('pause', self.player.state())
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
            self.pause_btn.setText('继续')
        if self.player.state() == QMediaPlayer.PausedState:
            pass

    def media_play_state_changed(self, state):
        if state == QMediaPlayer.PlayingState:
            print('playing state')

        if state == QMediaPlayer.PausedState:
            print('paused state')

        if state == QMediaPlayer.StoppedState:
            print('player stop state')

    def volumn_slider_value_changed(self, num):
        print('num', num)
        self.player.setVolume(num)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())
