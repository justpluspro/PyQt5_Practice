"""
视频下载工具
"""
import json
import sys
import time

from download_thread import DownloadThread
import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QHBoxLayout, QPushButton, QVBoxLayout, QTableWidget, \
    QHeaderView, QTableWidgetItem


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.download_table = None
        self.download_url = None
        self.download_btn = None
        self.download_thread = DownloadThread("")
        self.setWindowTitle("资源下载工具")
        self.resize(1080, 720)
        self.init_ui()

    def init_ui(self):
        top_layout = QHBoxLayout()
        self.download_url = QLineEdit()
        self.download_btn = QPushButton('下载')
        self.download_url.setPlaceholderText('请输入下载地址，以 http 开头')
        top_layout.addWidget(self.download_url)
        top_layout.addWidget(self.download_btn)
        # 设置布局在上面
        top_layout.setAlignment(Qt.AlignTop)

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
        self.download_btn.clicked.connect(self.start_download)

    def start_download(self):
        self.download_thread.download_url = self.download_url.text()
        self.download_thread.start()

        """将线程的触发器关联到指定方法上去"""
        self.download_thread.trigger.connect(self.display_progress)

    def display_progress(self, args):
        # print('收到线程执行信号. ', args)
        data = json.loads(args)
        row_count = self.download_table.rowCount()
        # self.download_table.setRowCount(row_count + 1)
        # self.download_table.setItem(row_count + 1, 0, QTableWidgetItem(data['url']))
        # self.download_table.setItem(row_count + 1, 1, QTableWidgetItem('名称'))
        # self.download_table.setItem(row_count + 1, 2, QTableWidgetItem(data['progress']))
        #
        url = data['url']
        progress = data['progress']
        print(f'下载地址{url} 下载进度{progress}')


def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
