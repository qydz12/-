# PySide6 科技风车辆实时监测系统（按照效果图设计）
# 文件名：vehicle_monitor_pro.py

import sys
import cv2
from ultralytics import YOLO

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QFileDialog,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QSizePolicy,
)

from PySide6.QtGui import (
    QImage,
    QPixmap,
    QFont,
)

from PySide6.QtCore import (
    Qt,
    QTimer,
    QDateTime,
)


class VehicleMonitor(QWidget):
    def __init__(self):
        super().__init__()

        # ============================
        # YOLO 模型
        # ============================
        self.model = YOLO("yolo11n.pt")

        self.vehicle_classes = [
            "car",
            "truck",
            "bus",
            "motorcycle",
        ]

        # ============================
        # 主窗口
        # ============================
        self.setWindowTitle("车辆实时监测系统")
        self.resize(1600, 900)

        self.setStyleSheet("""
            QWidget{
                background-color:#08111f;
                color:white;
                font-family:Microsoft YaHei;
            }
        """)

        # ============================
        # 顶部栏
        # ============================
        self.top_frame = QFrame()
        self.top_frame.setFixedHeight(90)

        self.top_frame.setStyleSheet("""
            QFrame{
                background:qlineargradient(
                    x1:0,y1:0,x2:1,y2:1,
                    stop:0 #0a1628,
                    stop:1 #07101d
                );
                border:1px solid #1f3b5b;
                border-radius:15px;
            }
        """)

        self.time_label = QLabel()
        self.time_label.setFont(QFont("Microsoft YaHei", 14))

        self.title_label = QLabel("车辆实时监测系统")
        self.title_label.setFont(QFont("Microsoft YaHei", 28, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)

        self.count_label = QLabel("车辆总数：0")
        self.count_label.setFont(QFont("Microsoft YaHei", 18, QFont.Bold))
        self.count_label.setStyleSheet("color:#55ff55")

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.time_label)
        top_layout.addStretch()
        top_layout.addWidget(self.title_label)
        top_layout.addStretch()
        top_layout.addWidget(self.count_label)

        self.top_frame.setLayout(top_layout)

        # ============================
        # 视频区域
        # ============================
        self.video_frame = QFrame()

        self.video_frame.setMinimumHeight(650)

        self.video_label = QLabel()

        self.video_label.setAlignment(Qt.AlignCenter)

        self.video_label.setMinimumSize(800, 600)

        self.video_label.setScaledContents(False)

        video_layout = QVBoxLayout()

        video_layout.addWidget(self.video_label)

        self.video_frame.setLayout(video_layout)
        # ============================
        # 按钮区域
        # ============================
        self.btn_camera = QPushButton("📷 打开摄像头")
        self.btn_video = QPushButton("📂 上传视频")
        self.btn_stop = QPushButton("■ 停止检测")

        self.btn_camera.setFixedHeight(65)
        self.btn_video.setFixedHeight(65)
        self.btn_stop.setFixedHeight(65)

        self.btn_camera.setStyleSheet("""
            QPushButton{
                background:qlineargradient(
                    x1:0,y1:0,x2:1,y2:1,
                    stop:0 #1d7fe2,
                    stop:1 #145999
                );
                border:none;
                border-radius:12px;
                font-size:24px;
                font-weight:bold;
                color:white;
            }

            QPushButton:hover{
                background:#2893ff;
            }
        """)

        self.btn_video.setStyleSheet("""
            QPushButton{
                background:qlineargradient(
                    x1:0,y1:0,x2:1,y2:1,
                    stop:0 #18a34a,
                    stop:1 #0b6e2f
                );
                border:none;
                border-radius:12px;
                font-size:24px;
                font-weight:bold;
                color:white;
            }

            QPushButton:hover{
                background:#1fcf5f;
            }
        """)

        self.btn_stop.setStyleSheet("""
            QPushButton{
                background:qlineargradient(
                    x1:0,y1:0,x2:1,y2:1,
                    stop:0 #d72f3c,
                    stop:1 #8d101a
                );
                border:none;
                border-radius:12px;
                font-size:24px;
                font-weight:bold;
                color:white;
            }

            QPushButton:hover{
                background:#ff4050;
            }
        """)

        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(20)
        btn_layout.addWidget(self.btn_camera)
        btn_layout.addWidget(self.btn_video)
        btn_layout.addWidget(self.btn_stop)

        # ============================
        # 底部状态栏
        # ============================
        self.bottom_frame = QFrame()
        self.bottom_frame.setFixedHeight(80)

        self.bottom_frame.setStyleSheet("""
            QFrame{
                background:qlineargradient(
                    x1:0,y1:0,x2:1,y2:1,
                    stop:0 #0a1628,
                    stop:1 #07101d
                );
                border:1px solid #1f3b5b;
                border-radius:12px;
            }
        """)

        self.video_path_label = QLabel("当前视频：无")
        self.video_path_label.setFont(QFont("Microsoft YaHei", 12))

        self.fps_label = QLabel("帧率：0 FPS")
        self.fps_label.setFont(QFont("Microsoft YaHei", 12))

        self.resolution_label = QLabel("分辨率：0 x 0")
        self.resolution_label.setFont(QFont("Microsoft YaHei", 12))

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.video_path_label)
        bottom_layout.addStretch()
        bottom_layout.addWidget(self.fps_label)
        bottom_layout.addSpacing(30)
        bottom_layout.addWidget(self.resolution_label)

        self.bottom_frame.setLayout(bottom_layout)

        # ============================
        # 主布局
        # ============================
        main_layout = QVBoxLayout()

        main_layout.addWidget(self.top_frame)
        main_layout.addSpacing(10)

        # 重点：视频区域占满空间
        main_layout.addWidget(self.video_frame, stretch=1)

        main_layout.addSpacing(10)
        main_layout.addLayout(btn_layout)
        main_layout.addSpacing(10)
        main_layout.addWidget(self.bottom_frame)

        self.setLayout(main_layout)

        # ============================
        # 定时器
        # ============================
        self.cap = None

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

        self.clock_timer = QTimer()
        self.clock_timer.timeout.connect(self.update_time)
        self.clock_timer.start(1000)

        # ============================
        # 信号绑定
        # ============================
        self.btn_camera.clicked.connect(self.open_camera)
        self.btn_video.clicked.connect(self.open_video)
        self.btn_stop.clicked.connect(self.stop_detection)

    # ============================
    # 更新时间
    # ============================
    def update_time(self):
        current_time = QDateTime.currentDateTime()

        time_str = current_time.toString(
            "yyyy-MM-dd hh:mm:ss"
        )

        self.time_label.setText(f"🕒 {time_str}")

    # ============================
    # 打开摄像头
    # ============================
    def open_camera(self):
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            return

        self.timer.start(30)

    # ============================
    # 上传视频
    # ============================
    def open_video(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "选择视频",
            "",
            "Video Files (*.mp4 *.avi *.mov)"
        )

        if file_path == "":
            return

        self.cap = cv2.VideoCapture(file_path)

        if not self.cap.isOpened():
            return

        self.video_path_label.setText(
            f"当前视频：{file_path}"
        )

        self.timer.start(30)

    # ============================
    # 更新视频帧
    # ============================
    def update_frame(self):
        if self.cap is None:
            return

        ret, frame = self.cap.read()

        if not ret:
            self.stop_detection()
            return

        # ============================
        # YOLO 检测
        # ============================
        results = self.model(frame)

        vehicle_count = 0

        for result in results:
            boxes = result.boxes

            for box in boxes:
                cls_id = int(box.cls[0])
                cls_name = self.model.names[cls_id]

                if cls_name in self.vehicle_classes:

                    vehicle_count += 1

                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    conf = float(box.conf[0])

                    # 绿色框
                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 255, 0),
                        2
                    )

                    label = f"{cls_name} {conf:.2f}"

                    cv2.putText(
                        frame,
                        label,
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 255, 0),
                        2
                    )

        # ============================
        # 左上角统计
        # ============================
        cv2.putText(
            frame,
            f"Vehicle Count: {vehicle_count}",
            (30, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.2,
            (0, 0, 255),
            3
        )

        self.count_label.setText(
            f"车辆总数：{vehicle_count}"
        )

        # ============================
        # FPS 和分辨率
        # ============================
        fps = self.cap.get(cv2.CAP_PROP_FPS)

        h, w, ch = frame.shape

        self.fps_label.setText(
            f"帧率：{fps:.1f} FPS"
        )

        self.resolution_label.setText(
            f"分辨率：{w} x {h}"
        )

        # ============================
        # OpenCV 转 Qt
        # ============================
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        qt_image = QImage(
            rgb_frame.data,
            w,
            h,
            ch * w,
            QImage.Format_RGB888
        )

        pixmap = QPixmap.fromImage(qt_image)

        self.video_label.setPixmap(
            pixmap.scaled(
                self.video_label.width(),
                self.video_label.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

    # ============================
    # 停止检测
    # ============================
    def stop_detection(self):
        self.timer.stop()

        if self.cap:
            self.cap.release()

        self.video_label.clear()


# ============================
# 主程序入口
# ============================
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = VehicleMonitor()
    window.show()

    sys.exit(app.exec())
