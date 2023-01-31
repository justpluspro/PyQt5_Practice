import sys

from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtWidgets import QWidget


def window():
    # 创建一个 QApplication 的应用程序对象
    app = QApplication(sys.argv)
    # 添加一个窗口控件
    w = QWidget()
    # 在窗口中添加一个标签
    b = QLabel(w)
    # 给标签设置了一个字符串，hello world
    b.setText('hello world')
    # 设置窗口位置和大小
    # 以 (100,100) 为左上顶点，宽设置为 200 高度设置为 50
    w.setGeometry(100, 100, 400, 300)

    # 设置标签的位置为（50，20）
    b.move(50, 20)

    # 设置窗口标题
    w.setWindowTitle('窗口标题')
    # 显示窗口
    w.show()

    # 进入事件主循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    """
        主方法
    """
    window()
