"""
QFileDialog.getOpenFileName() //选取文件
QFileDialog.getOpenFileNames() // 选取多个文件
QFileDialog.getExistingDirectory() // 选择目录
QFileDialog.getSaveFileName() //保存文件

以上方法均有多个参数，其中比较常用如下：
1. parent 一般选择为主窗体，先写 self
2. 文件选择框标题
3. 文件选择对话框当前打开的路径
4. 文件选择器
    - 选择所有文件 All(*)
    - 选择后缀为 mp4 的文件  mp4 files(*.mp4)
    - 选择后缀为 mp4、avi 的文件 mp4 files(*.mp4);;avi files(*.avi)


以上的方法有两个返回值
一个为 choose_filename, 该值会返回选择的文件路径（绝对路径）
另一个为 fType, 该值会返回当前窗口的文件选择器

如果是选择多个文件，则返回的 choose_filename 为一个数组

"""
import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication, QFileDialog


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.resize(300, 400)
        self.setWindowTitle('QFileDialog')

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        self.btn = QPushButton('选择单个文件')
        self.btn.clicked.connect(self.choose_file)

        self.btn2 = QPushButton('选择多个文件')
        self.btn2.clicked.connect(self.choose_files)

        self.btn3 = QPushButton('选择文件夹')
        self.btn3.clicked.connect(self.choose_dir)

        self.btn4 = QPushButton('保存文件')
        self.btn4.clicked.connect(self.save_file)

        self.btn5 = QPushButton('选择视频')
        self.btn5.clicked.connect(self.choose_video)

        layout.addWidget(self.btn)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.addWidget(self.btn4)
        layout.addWidget(self.btn5)
        self.setLayout(layout)

    def choose_file(self):
        choose_file, ftype = QFileDialog.getOpenFileName(self, '打开文件',
                                                         os.getcwd(), 'All files(*.*)')
        if choose_file == '':
            print('未选择文件')
        print('您选择的文件为', choose_file)

    def choose_files(self):
        choose_files, ftype = QFileDialog.getOpenFileNames(self, 'Open file',
                                                           'C:\\', "jpg files (*.jpg);; png files('*.png')")
        if len(choose_files) == 0:
            print('未选择文件')
        print('您选择的文件为', choose_files)

    def choose_dir(self):
        dir_choose = QFileDialog.getExistingDirectory(self, '选择目录', os.getcwd())
        if dir_choose == '':
            print('取消选择目录')
            return
        print('你选择的目录为:', dir_choose)

    def save_file(self):
        filename_choose, ftype = QFileDialog.getSaveFileName(self, '保存文件', os.getcwd(), 'All Files(*)')
        if filename_choose == '':
            print('取消保存')
            return

        print('你要保存的文件为：' + filename_choose)
        print('文件筛选器', ftype)

    def choose_video(self):
        filename_choose, ftype = QFileDialog.getOpenFileName(self, '选择视频', os.getcwd(), 'Mp4 file(*.mp4)')
        if filename_choose == '':
            print('取消选择')
            return
        print('您要选择的视频为', filename_choose)
        print('文件筛选器,', ftype)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
