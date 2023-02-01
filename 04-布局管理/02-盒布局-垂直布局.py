"""
一组放置在同一垂直线上的控件
"""

import sys

from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QVBoxLayout


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        button01 = QPushButton("01", self)
        button02 = QPushButton("02", self)
        button03 = QPushButton("03", self)
        button04 = QPushButton("04", self)

        layout = QVBoxLayout()
        # 将 button01 02 03 04 垂直排布
        layout.addWidget(button01)
        layout.addWidget(button02)
        # layout.addStretch(2)
        layout.addWidget(button03)
        # 在 03 和 04 之前添加一个类似弹簧的组件，可以将 04 挤到最下边
        # addStretch 方法中的参数表示将所有空闲的区域按照比例进行分配
        layout.addStretch(1)
        layout.addWidget(button04)

        self.setLayout(layout)

        self.setWindowTitle('盒布局-垂直布局')
        # 窗口定位到 （300， 300）位置，高 300，宽 150
        self.setGeometry(300, 300, 150, 300)
        self.show()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
