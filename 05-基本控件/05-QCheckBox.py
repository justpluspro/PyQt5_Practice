"""
复选框
"""
import sys

from PyQt5.QtWidgets import QVBoxLayout, QApplication, QWidget, QHBoxLayout, QCheckBox, QPushButton


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.resize(400, 300)
        self.setWindowTitle("QCheckBox")
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()

        self.btn1 = QCheckBox('button1')
        self.btn2 = QCheckBox('button2')
        # 关联状态选中
        self.btn1.stateChanged.connect(lambda: self.btn_state(self.btn1))
        self.btn2.stateChanged.connect(lambda: self.btn_state(self.btn2))

        """设置选中状态"""
        btn3 = QCheckBox('button3')
        btn3.setChecked(True)

        """设置不可选中"""
        btn4 = QCheckBox("button4")
        btn4.setEnabled(False)

        """检查按钮是否被选中"""
        btn5 = QPushButton('检查')
        btn5.clicked.connect(self.get_state)

        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        layout.addWidget(btn5)
        self.setLayout(layout)

    def btn_state(self, checkbox):
        if checkbox.text() == 'button1':
            if checkbox.isChecked():
                print('button1 checked')
            else:
                print('button1 unchecked')

        elif checkbox.text() == 'button2':
            if checkbox.isChecked():
                print('button2 checked')
            else:
                print('button2 unchecked')

    def get_state(self):
        print(self.btn1.isChecked())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
