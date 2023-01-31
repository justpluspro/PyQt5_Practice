import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QLineEdit


class MainWindow(QWidget):
    """
    信号和槽
    """
    def __init__(self):
        super().__init__()

        button1 = QPushButton(self)
        button1.move(200, 100)
        button1.setText('button1')
        # 将 button1 点击的事件绑定到定义好的 button_clicked 上去
        button1.clicked.connect(button_clicked)

        button2 = QPushButton(self)
        button2.setText('button2')
        button2.move(200, 200)
        # 将 button2 点击的事件绑定到定义好的 button_clicked2 上去
        button2.clicked.connect(button_clicked2)


        self.lineEdit = QLineEdit(self)
        # 设置坐标位置
        self.lineEdit.move(350, 300)
        # 设置文本
        self.lineEdit.setText('hello world')

        button3 = QPushButton(self)
        # 设置文本
        button3.setText('button3')
        # 设置坐标位置
        button3.move(200, 300)
        # 将 button3 点击的时间绑定到 QLineEdit 控件本身的 clear 方法上去
        # 点击即会清除 self.lineEdit 中的文本内容
        button3.clicked.connect(self.lineEdit.clear)
def button_clicked():
    """
    button 点击触发
    :return:
    """
    print('button clicked.')

def button_clicked2():
    """
    button2 点击触发
    :return:
    """
    print('button2 clicked')

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
