"""
窗口菜单
1. 要实现窗口菜单，自定义的类需要继承 QMainWindow
2. 分为两种，一种是菜单（menu），一种是动作（action）
- 动作是点击后，具体执行的逻辑，
- 菜单可以添加动作

3. 还有一种浮动菜单
"""
import sys

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction


class AppWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(700, 400)
        self.setWindowTitle("QMenuBar")
        self.init_ui()

    def init_ui(self):
        bar = self.menuBar()
        # 添加一个 File 一级菜单
        file = bar.addMenu("File")
        file.addAction("Open")
        # 添加一个 New 一级菜单
        new = bar.addMenu("New")
        ## 给 new 添加动作
        new.addAction('创建新文件')


        # 通过 Action 添加第三个菜单
        setting = QAction("Settings", self)
        setting.setShortcut("Ctrl+S")
        bar.addAction(setting)

        # 给 file 菜单添加子菜单
        edit = file.addMenu("Edit")
        copy = edit.addAction("Copy")
        copy.setShortcut("Ctrl+C")
        edit.addAction("Paste")

        # 给 file 菜单绑定事件
        file.triggered[QAction].connect(self.process_triggered)

        """图标菜单"""
        log_action = QAction(QIcon(QPixmap("data/logo.jpg")), "图标", self)
        bar.addAction(log_action)

    def process_triggered(self, q):
        print(q.text() + " is triggered")
def main():
    app = QApplication(sys.argv)
    window = AppWidget()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

