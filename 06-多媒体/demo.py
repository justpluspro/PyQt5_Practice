import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QWidget, QApplication
from playsound import playsound

from PyQt5 import QtWidgets, QtCore, QtMultimedia
import sys

app = QtWidgets.QApplication(sys.argv)
url = QtCore.QUrl.fromLocalFile(r"E:\PyQt5_Practice\06-多媒体\1.mp3")
content = QtMultimedia.QMediaContent(url)
player = QtMultimedia.QMediaPlayer()
player.setMedia(content)
player.setVolume(50)
player.play()
print(player.mediaStatus())
print(QMediaPlayer.NoMedia)
sys.exit(app.exec())
