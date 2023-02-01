"""
网格布局类似于表格一样
创建一个简单的表单提交
"""
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QLineEdit, QTextEdit


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        author_label = QLabel('作者')
        mail_label = QLabel('邮箱')
        feedback_label = QLabel('反馈')

        author_edit = QLineEdit()
        mail_edit = QLineEdit()
        feedback_edit = QTextEdit()
        # author_label 第1行第0列
        layout.addWidget(author_label, 1, 0)
        # author_edit 第1行第1列
        layout.addWidget(author_edit, 1, 1)
        # mail_label 第2行第0列
        layout.addWidget(mail_label, 2, 0)
        # mail_edit 第2行第1列
        layout.addWidget(mail_edit, 2, 1)
        # feedback_label 第3行第0列
        layout.addWidget(feedback_label, 3, 0)
        # feedback_edit 第3行第1列，占用5行高度，1行宽度
        layout.addWidget(feedback_edit, 3, 1, 5, 1)
        # 设置水平+垂直方向的间隙
        # layout.setSpacing(20)
        # 设置布局水平方向的间隙
        layout.setHorizontalSpacing(20)
        # 设置布局垂直方向的间隙
        layout.setVerticalSpacing(10)

        self.setLayout(layout)
        self.setWindowTitle("提交表单")
        self.show()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
