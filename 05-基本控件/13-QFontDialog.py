"""
QFontDialog 显示字体，弹出一个字体选择框，选择完字体后，将选择后的字体应用到 label 标签上
"""

import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QApplication, QFontDialog


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        button = QPushButton('选择字体')
        self.label = QLabel('中文 HelloWorld')

        button.clicked.connect(self.show_font_dialog)

        layout.addWidget(button)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def show_font_dialog(self):
        font, ok = QFontDialog.getFont(self)
        if ok:
            self.label.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
