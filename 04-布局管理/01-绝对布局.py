"""
绝对布局采用固定的点位来确定布局，
1、不会因为窗口的变化而变化
2、更换字体或者不同分辨率的显示器会破坏布局
3、如果不设置布局，那么将采用绝对布局（绝对布局是默认布局）
4、使用 move() 来定位元素

"""
import sys

from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        label1 = QLabel('label1', self)
        # 从（15，10）开始
        label1.move(15, 10)

        label2 = QLabel('label2', self)
        # 从（35，40）开始
        label2.move(35, 40)

        label3 = QLabel('label3', self)
        # 从（55，70）开始
        label3.move(55, 70)

        self.setWindowTitle('绝对布局')
        # 窗口定位到 （300， 300）位置，宽 250，高 150
        self.setGeometry(300, 300, 250, 150)
        self.show()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
