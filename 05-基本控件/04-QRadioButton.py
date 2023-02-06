"""
单选按钮
"""
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QRadioButton, QHBoxLayout, QButtonGroup


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.resize(400, 300)
        self.setWindowTitle("QRadioButton")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        """普通 RadioButton"""
        radio_btn = QRadioButton()
        radio_btn.setText('选择')

        """设置选中状态"""
        hlayout = QHBoxLayout()
        man_radio_btn = QRadioButton()
        man_radio_btn.setText('男')
        # 默认选中男
        man_radio_btn.setChecked(True)
        woman_radio_btn = QRadioButton()
        woman_radio_btn.setText('女')

        hlayout.addWidget(man_radio_btn)
        hlayout.addWidget(woman_radio_btn)

        """检查按钮选中状态"""
        self.checked_state_radio_btn = QRadioButton()
        self.checked_state_radio_btn.setText('选中')
        self.checked_state_radio_btn.clicked.connect(self.get_state)

        layout.addWidget(radio_btn)
        layout.addWidget(self.checked_state_radio_btn)
        layout.addLayout(hlayout)

        self.setLayout(layout)

    def get_state(self):
        print(f'{self.checked_state_radio_btn.isChecked()}')


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
