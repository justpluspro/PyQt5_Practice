import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QWidget, QApplication
from playsound import playsound


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.player = QMediaPlayer(self)
        self.file_path = '1.mp3'
        url = QUrl.fromLocalFile(self.file_path)
        self.media_content = QMediaContent(url)
        self.player.setMedia(self.media_content)
        self.player.setVolume(80)
        self.player.play()

    def init_ui(self):
        self.setWindowTitle('播放音乐')
        self.resize(400, 500)
        # playsound('1.mp3')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
