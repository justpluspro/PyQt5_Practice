"""
视频下载工具
"""
import sys

import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QHBoxLayout, QPushButton, QVBoxLayout, QTableWidget, \
    QHeaderView, QTableWidgetItem


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.download_url = None
        self.download_btn = None
        self.setWindowTitle("资源下载工具")
        self.resize(1080, 720)
        self.init_ui()

    def init_ui(self):
        top_layout = QHBoxLayout()
        self.download_url = QLineEdit()
        self.download_btn = QPushButton('下载')
        self.download_url.setPlaceholderText('请输入下载地址，以 http 开头')
        self.download_url.setText(
            'http://bj.download.cycore.cn/zhkt/2023/1/7/4/18/cf84c985-b19c-4db7-b702-963641ff24ba.mp4')
        top_layout.addWidget(self.download_url)
        top_layout.addWidget(self.download_btn)

        self.download_table = QTableWidget()
        font = QFont('微软雅黑')
        font.setBold(True)
        # 设置表头字体
        self.download_table.horizontalHeader().setFont(font)
        self.download_table.horizontalHeader().setFixedHeight(50)  ##设置表头高度
        self.download_table.setColumnCount(3)  # 设置表格一共有三列
        self.download_table.setHorizontalHeaderLabels(['下载链接', '大小', '进度'])
        # 设置表头禁止点击
        self.download_table.horizontalHeader().setSectionsClickable(False)
        # 设置最后一列拉伸至最大
        # self.download_table.horizontalHeader().setStretchLastSection(True)
        # 设置第一列宽度自动调整，拉伸到最大
        self.download_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.download_table)

        self.setLayout(main_layout)

        """绑定点击事件"""
        self.download_btn.clicked.connect(lambda: self.start_download(self.download_url))

    def start_download(self, download_url):
        url = download_url.text()
        row_count = self.download_table.rowCount()
        # data = {url, '名称', '0%'}
        self.download_table.setItem(row_count + 1, 0, QTableWidgetItem(url))
        self.download_table.setItem(row_count + 1, 1, QTableWidgetItem('名称'))
        self.download_table.setItem(row_count + 1, 2, QTableWidgetItem('0%'))

        print(url)
        """stream=True 表示使用流式下载"""
        response = requests.get(url, stream=True)
        total_length = int(response.headers.get('Content-Length'))
        chunk_size = 1024
        offset = 0
        with open('video.mp4', "wb") as file:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    offset += chunk_size
                    file.write(chunk)
                    download_progress = '%.2f' % ((offset / total_length) * 100)
                    print(f'总大小: {total_length}')
                    print(f'下载大小: {offset}')
                    print(f'当前下载进度: {download_progress}')


def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
