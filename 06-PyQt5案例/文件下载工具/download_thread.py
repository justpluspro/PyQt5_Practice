import json

import requests
from PyQt5.QtCore import QThread, pyqtSignal


class DownloadThread(QThread):
    """定义信号"""
    trigger = pyqtSignal(str)
    """
    下载线程
    """
    def __init__(self, download_url):
        super().__init__()
        self.download_url = download_url

    def run(self):
        """stream=True 表示使用流式下载"""
        response = requests.get(self.download_url, stream=True)
        total_length = int(response.headers.get('Content-Length'))
        chunk_size = 1024
        offset = 0
        print(f'开始下载{self.download_url}')
        with open('video.mp4', "wb") as file:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    offset += chunk_size
                    file.write(chunk)
                    download_progress = '%.2f' % ((offset / total_length) * 100)
                    # print(f'总大小: {total_length}')
                    # print(f'下载大小: {offset}')
                    # print(f'当前下载进度: {download_progress}')
                    self.trigger.emit(json.dumps({'url': self.download_url, 'progress': download_progress}))