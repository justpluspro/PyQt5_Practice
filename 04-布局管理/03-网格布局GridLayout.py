"""
网格布局类似于表格一样

通过对象的 addWidget() 方法来添加控件

addWidget(控件，网格横坐标，网格纵坐标)
addWidget(控件，网格横坐标，网格纵坐标，占用行数，占用列数)
"""
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()
        # 双层循环，在每个网格中放置一个按钮
        # 定义一个 4 行 4 列的网格
        for i in range(1, 5):
            for j in range(1, 5):
                layout.addWidget(QPushButton("B" + str(i) + str(j)), i, j)
        self.setLayout(layout)
        self.show()

        self.setWindowTitle("网格布局")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
