import sys

from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QLabel, QApplication

"""Tab 需要控件继承 QTabWidget"""


class MainWindow(QTabWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setWindowTitle("Tab Demo")

    def init_ui(self):
        """创建三个 tab"""
        self.tab_1 = QWidget()
        self.tab_2 = QWidget()
        self.tab_3 = QWidget()

        self.addTab(self.tab_1, "tab_1")
        self.addTab(self.tab_2, "tab_2")
        self.addTab(self.tab_3, "tab_3")

        self.tab_ui('tab_1')
        self.tab_ui('tab_2')
        self.tab_ui('tab_3')

        # 设置选项卡的位置在南边
        self.setTabPosition(QTabWidget.East)

        # 设置当前选中的是索引为1的
        self.setCurrentIndex(1)

        # 给tab设置文本
        self.setTabText(0, '张三')

        """监听 tab 的切换"""
        self.currentChanged.connect(self.tab_index_changed)

    def tab_ui(self, label_name):
        layout = QVBoxLayout()
        layout.addWidget(QLabel(label_name))
        if label_name == 'tab_1':
            self.tab_1.setLayout(layout)
        if label_name == 'tab_2':
            self.tab_2.setLayout(layout)
        if label_name == 'tab_3':
            self.tab_3.setLayout(layout)

    def tab_index_changed(self, index):
        """index 从 0 开始"""
        print(index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
