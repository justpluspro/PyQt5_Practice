"""
QLabel 可以用来展示 字符串，超链接，富文本，图片等
"""
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication, QPushButton


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # 普通文本
        normal_label = QLabel("普通文本")

        # 图片
        image_label = QLabel()
        image_label.setPixmap(QPixmap("data/logo.jpg"))
        """窗口大小发生变化时，图片是否跟随缩放"""
        # image_label.setScaledContents(True)

        # 超链接
        link_label = QLabel()
        """设置富文本类型"""
        link_label.setText('<a href="https://www.baidu.com">百度一下，你就知道</a>')
        """设置超链接可以被点击打开"""
        link_label.setOpenExternalLinks(True)
        """设置鼠标可选中，如果设置了该选项，超链接将无法被打开"""
        # link_label.setTextInteractionFlags(Qt.TextSelectableByMouse)

        link_label.linkActivated.connect(link_activated)
        link_label.linkHovered.connect(link_hovered)

        """设置字体"""
        font = QFont()
        font.setFamily('微软雅黑')
        font.setPointSize(24)
        normal_label.setFont(font)

        """获取标签内容"""
        button = QPushButton('获取标签内容')
        button.clicked.connect(lambda: get_label1_text(normal_label))

        layout.addWidget(normal_label)
        layout.addWidget(image_label)
        layout.addWidget(link_label)
        layout.addWidget(button)
        self.setLayout(layout)
        self.setWindowTitle('QLabel')
        self.show()


def link_activated():
    print('link_activated')


def link_hovered():
    print('link_hovered')


def get_label1_text(label):
    print(label.text())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
