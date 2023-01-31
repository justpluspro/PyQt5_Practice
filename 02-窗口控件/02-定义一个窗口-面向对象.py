import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtWidgets import QWidget


class Window(QWidget):
    """
    面向对象版本一个简单的窗口程序
    """

    def __init__(self):
        """
        申明构造方法
        """
        super().__init__()
        # 设置当前 Window 对象的大小
        self.resize(400, 300)
        # 设置（100，100）为左上顶点，不设置则窗口默认居中显示
        # self.move(100, 100)
        # 在窗口中添加一个标签
        self.label = QLabel(self)
        # 给标签设置了一个字符串，hello world
        self.label.setText('hello world')

        # 设置窗口标题
        self.setWindowTitle('窗口标题')

        # 设置字体
        font = QFont()
        font.setFamily('Arial')
        font.setPointSize(24)
        self.label.setFont(font)

        # 设置标签的位置为（50，20）
        self.label.move(50, 20)


def main():
    # 创建一个 QApplication 的应用程序对象
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    # 进入事件主循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    """
        主方法
    """
    main()
