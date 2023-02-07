"""
工具栏，浮动的状态，可以拖动
"""
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction


class AppWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(700, 400)
        self.setWindowTitle("QToolbar")
        self.init_ui()
    def init_ui(self):
        """添加普通 toolbar"""
        tb = self.addToolBar("File")
        new = QAction(QIcon("data/logo.jpg"), "new", self)
        tb.addAction(new)

def main():
    app = QApplication(sys.argv)
    window = AppWidget()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
