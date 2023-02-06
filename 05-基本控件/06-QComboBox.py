"""
 下拉框
"""

import sys

from PyQt5.QtWidgets import QVBoxLayout, QApplication, QWidget, QHBoxLayout, QCheckBox, QPushButton, QComboBox, QLabel


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.resize(400, 300)
        self.setWindowTitle("QComboBox")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        """简单下拉框"""
        label1 = QLabel('简单下拉框')
        combo_box = QComboBox()
        combo_box.addItem('张三')
        combo_box.addItem('李四')
        combo_box.addItem('王五')

        """列表下拉框"""
        label2 = QLabel('列表下拉框')
        list_combo_box = QComboBox()
        list_combo_box.addItems(['java', 'android', 'js', 'kotlin'])

        """默认选中"""
        label3 = QLabel('默认选中index=2')
        default_checked_combo_box = QComboBox()
        default_checked_combo_box.addItems(['java', 'android', 'js', 'kotlin'])
        # 索引从 0 开始，默认选中下标为 2 的下拉框
        default_checked_combo_box.setCurrentIndex(2)

        """禁用下拉框"""
        label4 = QLabel('禁用下拉框=2')
        disabled_combo_box = QComboBox()
        disabled_combo_box.addItems(['java', 'android', 'js', 'kotlin'])
        disabled_combo_box.setEnabled(False)

        """选中触发"""
        label5 = QLabel('选中触发')
        changed_combo_box = QComboBox()
        changed_combo_box.addItems(['java', 'android', 'js', 'kotlin'])
        changed_combo_box.currentIndexChanged.connect(lambda: self.value_changed(changed_combo_box))

        """追加内容"""
        label6 = QLabel('追加内容')
        append_combo_box = QComboBox()
        append_combo_box.addItem('css')
        append_combo_box.addItems(['java', 'android', 'js', 'kotlin'])

        layout.addWidget(label1)
        layout.addWidget(combo_box)
        layout.addWidget(label2)
        layout.addWidget(list_combo_box)
        layout.addWidget(label3)
        layout.addWidget(default_checked_combo_box)
        layout.addWidget(label4)
        layout.addWidget(disabled_combo_box)
        layout.addWidget(label5)
        layout.addWidget(changed_combo_box)
        layout.addWidget(label6)
        layout.addWidget(append_combo_box)
        self.setLayout(layout)


    def value_changed(self, combo_box):
        index = combo_box.currentIndex()
        value = combo_box.currentText()
        print({'index': index, 'value': value})

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()