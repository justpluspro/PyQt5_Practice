import sys

import cv2
from PyQt5 import QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QMessageBox, QApplication


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        # 定义定时器，控制显示视频的帧率
        self.timer_camera = QtCore.QTimer()
        self.cap = cv2.VideoCapture()
        self.CAM_NUM = 0

        """初始化界面"""
        self.init_ui()
        self.init_slot_ui()

    def init_ui(self):

        self.main_layout = QHBoxLayout()
        self.fun_button_layout = QVBoxLayout()
        self.data_show_layout = QVBoxLayout()

        self.button_open_camera = QPushButton('打开相机')
        self.button_close_camera = QPushButton('退出')
        self.button_take_photo = QPushButton('抓图')
        self.button_open_camera.setMinimumHeight(50)
        self.button_close_camera.setMinimumHeight(50)
        self.button_take_photo.setMinimumHeight(50)

        self.button_close_camera.move(10, 100)

        self.label_show_camera = QLabel()
        self.label_show_camera.setFixedSize(641, 481)

        """将按键加入布局"""
        self.fun_button_layout.addWidget(self.button_open_camera)
        self.fun_button_layout.addWidget(self.button_close_camera)
        self.fun_button_layout.addWidget(self.button_take_photo)

        self.main_layout.addLayout(self.fun_button_layout)
        self.main_layout.addWidget(self.label_show_camera)

        self.setLayout(self.main_layout)

    def init_slot_ui(self):
        self.button_open_camera.clicked.connect(self.button_open_camera_clicked)
        # 将定时器的 timeout 方法绑定到 show_camera 上去
        self.timer_camera.timeout.connect(self.show_camera)
        self.button_close_camera.clicked.connect(self.close)
        self.button_take_photo.clicked.connect(self.button_take_photo_clicked)

    def button_open_camera_clicked(self):
        """
        打开摄像头画面
        :return:
        """
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:  # 这里的 flag 表示 open() 是否成功
                msg = QMessageBox.warning(self, 'warning', '请检查电脑相机是否连接正确', QMessageBox.Ok)
            else:
                # 定时器开始计时，每过 30ms 从摄像头取一帧画面显示
                self.timer_camera.start(30)
                self.button_open_camera.setText('关闭相机')
        else:
            self.timer_camera.stop()
            self.cap.release()
            self.label_show_camera.clear()
            self.button_open_camera.setText('打开相机')

    def show_camera(self):
        flag, self.image = self.cap.read()  # 从视频流中读取图片
        show = cv2.resize(self.image, (640, 480))  # 将读取到的图片调整至 640 * 480 大小
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)  # 视频色彩转换成 rgb
        # 将读到的视频数转换成 QImage
        show_image = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        # 显示到 label 上
        self.label_show_camera.setPixmap(QPixmap.fromImage(show_image))

    def button_take_photo_clicked(self):
        """定时器是否激活，没有激活说明摄像头没有打开"""
        if self.timer_camera.isActive():
            cv2.imwrite('pic_capture.jpg', self.image)
            # 抓图后，显示结果
        else:
            msg = QMessageBox.warning(self, 'warning', '请先打开摄像头再抓图', QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
