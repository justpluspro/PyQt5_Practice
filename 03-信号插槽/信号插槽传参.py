import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLineEdit


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        button1 = QPushButton(self)
        button1.move(100, 100)
        button1.setText('button1')
        # 使用 lambda 表达式传递普通文本
        button1.clicked.connect(lambda: button_clicked(10))

        button2 = QPushButton(self)
        button2.move(100, 200)
        button2.setText('button2')
        # 使用 lambda 表达式传递对象引用
        button2.clicked.connect(lambda: button_clicked2(self.line_edit))


        self.line_edit = QLineEdit(self)
        self.line_edit.setText('hello world')
        self.move(100, 50)


def button_clicked(count):
    print(count)


def button_clicked2(line_edit):
    line_edit.setText('更改后的值')

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
