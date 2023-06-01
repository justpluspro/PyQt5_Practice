
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QDropEvent

class ChooseFileTextArea(QTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置接受拖拽
        self.setAcceptDrops(True)
        # 设置为只读状态
        self.setReadOnly(True)
        self.setText('选择文件')
        self.setMinimumHeight(96)
        self.setStyleSheet('background-color: red; border-radius: 4px; text-align: center')

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        urls = [u for u in event.mimeData().urls()]
        for url in urls:
            print(url.path()[1:])

