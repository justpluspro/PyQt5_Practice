"""
滑块
"""
from PyQt5.QtGui import QFont

"""
滑块
根据滑块的变化，动态改变 label 标签的字体大小

"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QWidget, QHBoxLayout, QCheckBox, QPushButton, QComboBox, QLabel, \
    QSpinBox, QSlider


class MainWindow(QWidget):
    count = 0
    def __init__(self):
        super().__init__()

        self.resize(400, 300)
        self.setWindowTitle("QSlider")
        self.init_ui()

    def init_ui(self):

        self.font = QFont()
        self.font.setFamily('微软雅黑')
        self.font.setPointSize(16)

        label = QLabel('hello')
        label.setFont(self.font)
        slider = QSlider(Qt.Horizontal)
        # 设置范围
        slider.setRange(1, 48)
        # 设置步长
        slider.setPageStep(2)

        slider.setSingleStep(2)
        # 设置默认值为 16
        slider.setValue(16)

        # 设置刻度线
        ## 下方刻度线
        # slider.setTickPosition(QSlider.TicksBelow)
        ## 兩方刻度綫
        slider.setTickPosition(QSlider.TicksBothSides)

        slider.valueChanged.connect(lambda: self.value_changed(label, slider))

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(slider)

        self.setLayout(layout)
    def value_changed(self, label, slider):
        value = slider.value()
        self.font.setPointSize(value)
        label.setFont(self.font)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()