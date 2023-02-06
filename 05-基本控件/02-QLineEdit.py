"""
QLineEdit 是一个单行文本框
"""
import sys

from PyQt5.QtGui import QDoubleValidator, QFont, QIntValidator
from PyQt5.QtWidgets import QWidget, QLineEdit, QApplication, QVBoxLayout


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        # 设置窗口标题
        self.setWindowTitle('QLineEdit')
        # self.setGeometry(300, 400, 400, 400)
        self.resize(720, 400)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        """普通输入框"""
        self.line_edit_normal = QLineEdit(self)
        self.line_edit_normal.setText('测试')

        """设置最大字符"""
        self.max_count_edit = QLineEdit(self)
        self.max_count_edit.setMaxLength(10)
        self.max_count_edit.setText('最大字符10个')

        """设置输入模式"""
        self.edit_mode = QLineEdit(self)
        # 密码输入
        self.edit_mode.setEchoMode(QLineEdit.Password)
        self.edit_mode.setText("123456")
        # 设置输入格式，文本或者密码
        # self.line_edit.setEchoMode(QLineEdit.Password)
        # self.line_edit.setEchoMode(QLineEdit.EchoMode.NoEcho)
        # self.line_edit.setDragEnabled(True)

        """设置只读"""
        self.readonly_edit = QLineEdit(self)
        self.readonly_edit.setReadOnly(True)
        self.readonly_edit.setText('只读')

        """设置字体"""
        font = QFont()
        font.setFamily('微软雅黑')
        font.setPointSize(18)
        self.font_size_edit = QLineEdit(self)
        self.font_size_edit.setFont(font)
        self.font_size_edit.setText('字体')

        """设置掩码"""
        inputmask_edit = QLineEdit(self)
        # 电话号码掩码
        inputmask_edit.setInputMask('+99_999_9999_9999')

        """文本改变信号"""
        text_change_edit = QLineEdit(self)
        text_change_edit.textChanged.connect(self.text_changed)

        """按下 enter 触发"""
        enter_press_edit = QLineEdit(self)
        enter_press_edit.setText('仅按下 enter 触发事件')
        enter_press_edit.returnPressed.connect(self.return_pressed)

        """失去焦点后者输入完成(enter)触发"""
        finish_edit = QLineEdit(self)
        finish_edit.setText('失去焦点后者输入完成(enter)触发')
        finish_edit.editingFinished.connect(self.editing_finished)

        layout.addWidget(self.line_edit_normal)
        layout.addWidget(self.max_count_edit)
        layout.addWidget(self.edit_mode)
        layout.addWidget(self.readonly_edit)
        layout.addWidget(self.font_size_edit)
        layout.addWidget(inputmask_edit)
        layout.addWidget(text_change_edit)
        layout.addWidget(enter_press_edit)
        layout.addWidget(finish_edit)

        self.setLayout(layout)

    def text_changed(self):
        print('文本改变')

    def return_pressed(self):
        print('按下 enter 触发')

    def editing_finished(self):
        print('输入完成（enter）或者失去焦点触发')


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
