"""
按钮控件
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('QPushButton')
        self.resize(300, 400)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        """普通按钮"""
        btn1 = QPushButton('普通按钮')

        """图标按钮"""
        btn2 = QPushButton()
        btn2.setIcon(QIcon(QPixmap("data/logo.jpg")))

        """按钮禁用"""
        btn3 = QPushButton()
        btn3.setText('被禁用的按钮')
        btn3.setEnabled(False)

        """默认按钮"""
        btn4 = QPushButton()
        btn4.setText('&Default')
        btn4.setDefault(True)

        """可选中按钮"""
        self.btn5 = QPushButton("可选中")
        self.btn5.setCheckable(True)
        # 设置鼠标样式
        self.btn5.setCursor(Qt.BusyCursor)
        self.btn5.toggle()
        # 选中条件触发
        self.btn5.clicked.connect(self.btn_state)

        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        layout.addWidget(self.btn5)
        self.setLayout(layout)
        self.show()

    def btn_state(self):
        if self.btn5.isChecked():
            print('选中')
        else:
            print('取消选中')


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
