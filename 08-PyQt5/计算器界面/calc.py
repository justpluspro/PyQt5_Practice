
"""
实现计算器界面
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QGridLayout, QApplication, QPushButton


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('计算器')
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        input = QLineEdit()
        main_layout.addWidget(input)

        calc_layout = QGridLayout()
        calc_layout.addWidget(QPushButton("("), 1, 1)
        calc_layout.addWidget(QPushButton(")"), 1, 2)
        calc_layout.addWidget(QPushButton("back"), 1, 3)
        calc_layout.addWidget(QPushButton("Clear"), 1, 4)

        calc_layout.addWidget(QPushButton("7"), 2, 1)
        calc_layout.addWidget(QPushButton("8"), 2, 2)
        calc_layout.addWidget(QPushButton("9"), 2, 3)
        calc_layout.addWidget(QPushButton("/"), 2, 4)

        calc_layout.addWidget(QPushButton("4"), 3, 1)
        calc_layout.addWidget(QPushButton("5"), 3, 2)
        calc_layout.addWidget(QPushButton("6"), 3, 3)
        calc_layout.addWidget(QPushButton("*"), 3, 4)

        calc_layout.addWidget(QPushButton("1"), 4, 1)
        calc_layout.addWidget(QPushButton("2"), 4, 2)
        calc_layout.addWidget(QPushButton("3"), 4, 3)
        calc_layout.addWidget(QPushButton("-"), 4, 4)

        calc_layout.addWidget(QPushButton("0"), 4, 1)
        calc_layout.addWidget(QPushButton("."), 4, 2)
        calc_layout.addWidget(QPushButton("="), 4, 3)
        calc_layout.addWidget(QPushButton("+"), 4, 4)


        main_layout.addLayout(calc_layout)

        self.setLayout(main_layout)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
