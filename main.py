import sys
import cv2
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import QTimer,Qt
from design import Ui_MainWindow  # 导入从 .ui 文件生成的类
#from your_camera_module import CameraClass
class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 设置UI

        #self.camera = CameraClass()  # 实例化您的相机类
        # 连接按钮等控件的信号与槽
        self.connect_button.clicked.connect(self.start_camera)
        self.capture_button.clicked.connect(self.capture)
        self.camera_setting_button.clicked.connect(self.camera_setting)
        self.recording_button.clicked.connect(self.recording)
        self.stop_button.clicked.connect(self.stop)
        # ... 其他控件的信号槽连接 ...
        self.timer = QTimer(self)#计时器，用来控制update_frame的循环调用的频率，在start_camera函数中启动这个计时器，这里只做初始化
        self.timer.timeout.connect(self.update_frame)
    #停止计时器，即停止视频显示
    def stop(self):
        self.timer.stop()

    #更新帧的函数，真实情况这里需要调用相机函数获取当前帧，这个函数里现在六个图像都是一样的，实际需要处理
    def update_frame(self):
        ret,self.frame1=self.cap.read()
        if self.frame1 is not None:
            self.frame1 = cv2.cvtColor(self.frame1, cv2.COLOR_BGR2GRAY)
            self.frame2=self.frame1
            self.frame3 = self.frame1
            self.frame4 = self.frame1
            self.frame5 = self.frame1
            self.frame6 = self.frame1
            self.display()#更新完帧数后调用显示函数
    #把帧转换成Qt能使用的格式并显示
    def display(self):
        h, w = self.frame1.shape
        bytes_per_line = w
        q_img1 = QImage(self.frame1.data, w, h, bytes_per_line, QImage.Format.Format_Grayscale8)
        q_img2 = QImage(self.frame2.data, w, h, bytes_per_line, QImage.Format.Format_Grayscale8)
        q_img3 = QImage(self.frame3.data, w, h, bytes_per_line, QImage.Format.Format_Grayscale8)
        q_img4 = QImage(self.frame4.data, w, h, bytes_per_line, QImage.Format.Format_Grayscale8)
        q_img5 = QImage(self.frame5.data, w, h, bytes_per_line, QImage.Format.Format_Grayscale8)
        q_img6 = QImage(self.frame6.data, w, h, bytes_per_line, QImage.Format.Format_Grayscale8)
        pixmap1 = QPixmap.fromImage(q_img1)
        scaled_pixmap1 = pixmap1.scaled(self.l1.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.l1.setPixmap(scaled_pixmap1)
        pixmap2 = QPixmap.fromImage(q_img2)
        scaled_pixmap2 = pixmap2.scaled(self.l2.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.l2.setPixmap(scaled_pixmap2)
        pixmap3 = QPixmap.fromImage(q_img3)
        scaled_pixmap3 = pixmap3.scaled(self.l3.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.l3.setPixmap(scaled_pixmap3)
        pixmap4 = QPixmap.fromImage(q_img4)
        scaled_pixmap4 = pixmap4.scaled(self.l4.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.l4.setPixmap(scaled_pixmap4)
        pixmap5 = QPixmap.fromImage(q_img5)
        scaled_pixmap5 = pixmap5.scaled(self.l5.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.l5.setPixmap(scaled_pixmap5)
        pixmap6 = QPixmap.fromImage(q_img6)
        scaled_pixmap6 = pixmap6.scaled(self.l6.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.l6.setPixmap(scaled_pixmap6)
    def recording(self):
        print("recording")
    def camera_setting(self):
        print("camera_setting")
    def capture(self):
        print("capture")
    #启动计时器，开始显示
    def start_camera(self):
        self.cap = cv2.VideoCapture('1.1.mp4')
        self.timer.start(30)
        print("start camera")
        # 启动相机的逻辑
        #self.camera.start_camera()
        # 更新UI或其他操作

    # 定义其他方法，例如更新UI显示视频流等

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
