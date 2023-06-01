import json

import requests
from PyQt5.QtCore import QThread, pyqtSignal


class QueryWeatherThread(QThread):
    signal = pyqtSignal(str)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        # 设置请求头
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
        }
        print('开始查询城市信息：{}', self.url)
        response = requests.get(url=self.url, headers=headers)
        print(f'响应内容 {response.json()}')
        print(f'响应内容2 {response.text}')

        """json.loads 将json对象转换成 python 字典"""
        weather_info = json.loads(response.text)
        if str(weather_info['infocode']) == '10000' and str(weather_info['count']) == "1":
            city_info = weather_info['lives'][0]

            content = '城市:' + city_info['province'] + '\n' \
                      '天气:' + city_info['weather'] + '\n' \
                      '温度:' + city_info['temperature'] + '\n' \
                      '风向:' + city_info['winddirection'] + '\n'
        else:
            content = '天气查询有误'
        self.signal.emit(content)
