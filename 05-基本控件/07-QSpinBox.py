"""
输入框只能输入数字，且输入框有有计数标志
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QWidget, QHBoxLayout, QCheckBox, QPushButton, QComboBox, QLabel, \
    QSpinBox


class MainWindow(QWidget):
    count = 0
    def __init__(self):
        super().__init__()

        self.resize(400, 300)
        self.setWindowTitle("QSpinBox")
        self.init_ui()

    def init_ui(self):
        label = QLabel(f'当前计数 {self.count}')
        spin_box = QSpinBox()
        # 计数器上限
        spin_box.setMaximum(100)
        # 计数器下限
        spin_box.setMinimum(0)

        # 设置值
        spin_box.setValue(20)
        # 设置最小值，最大值，同范围设置
        # spin_box.setRange(0, 100)

        spin_box.valueChanged.connect(lambda: self.value_changed(label, spin_box))

        layout = QVBoxLayout()
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(spin_box, alignment=Qt.AlignmentFlag.AlignTop)

        self.setLayout(layout)
    def value_changed(self, label, spin_box):
        value = spin_box.value()
        label.setText(f'当前计数{value}')

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()