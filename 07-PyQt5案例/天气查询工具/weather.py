import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTextEdit, QApplication
from query_thread import QueryWeatherThread


class Weather(QWidget):
    def __init__(self):
        super().__init__()
        self.display = None
        self.query_btn = None
        self.input_edit = None
        self.resize(400, 300)
        self.init_ui()
        self.query_thread = QueryWeatherThread("")

    def init_ui(self):
        main_layout = QVBoxLayout()
        input_layout = QHBoxLayout()

        font = QFont()
        font.setFamily('微软雅黑')
        font.setPointSize(14)

        self.input_edit = QLineEdit()
        self.input_edit.setFont(font)
        self.input_edit.setPlaceholderText('请输入城市名称')
        self.query_btn = QPushButton('查询')
        self.query_btn.setFont(font)

        input_layout.addWidget(self.input_edit)
        input_layout.addWidget(self.query_btn)
        self.query_btn.clicked.connect(self.query_weather)

        main_layout.addLayout(input_layout)

        self.display = QTextEdit()
        self.display.setReadOnly(True)
        self.display.setFont(font)
        main_layout.addWidget(self.display)

        self.setLayout(main_layout)

    def query_weather(self):
        self.display.setText('')
        url = 'https://restapi.amap.com/v3/weather/weatherInfo?key=f4fd5b287b6d7d51a3c60fee24e42002&city=' + self.input_edit.text()
        self.input_edit.setText('')
        print(url)
        self.query_thread.url = url
        self.query_thread.start()
        self.query_thread.signal.connect(self.display_result)

    def display_result(self, result):
        content = '当前城市天气如下\n\n' + result
        self.display.setText(content)


def main():
    app = QApplication(sys.argv)
    window = Weather()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
