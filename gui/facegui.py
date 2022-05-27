from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets #pip install pyqt5(pip install python3-pyqt5)
from image import pi_camera
from mqtt_client import image_send,hair_setting_send
from picamera import PiCamera
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QPushButton
from gui import btn_control, info
import mqtt_client
import sys
from voice_control import kakao_voice
from user import status_check

return_hair_location = "./temp/return_image/"

hair_data = {
    'person_type' : '',
    'hair_type' : ''
}

photos = []
dots = []

def init_hair_gui(self,MainWindow):
    global photos, dots

    self.camera_timer = QtWidgets.QLabel(self.centralwidget)
    self.camera_timer.setGeometry(QtCore.QRect(950, 500, 1000, 150))
    self.camera_timer.setObjectName("info")
    self.camera_timer.setFont(QtGui.QFont("맑은 고딕",50))
    self.camera_timer.setStyleSheet("Color : white")

    self.photo1 = QtWidgets.QLabel(self.centralwidget)
    self.photo1.setGeometry(QtCore.QRect(450,150,10,60))
    self.photo1.resize(0,0)

    self.photo2 = QtWidgets.QLabel(self.centralwidget)
    self.photo2.setGeometry(QtCore.QRect(1000,150,10,60))
    self.photo2.resize(0,0)

    self.photo3 = QtWidgets.QLabel(self.centralwidget)
    self.photo3.setGeometry(QtCore.QRect(450,600,10,60))
    self.photo3.resize(0,0)

    self.photo4 = QtWidgets.QLabel(self.centralwidget)
    self.photo4.setGeometry(QtCore.QRect(1000,600,10,60))
    self.photo4.resize(0,0)

    self.dot1 = QtWidgets.QLabel(self.centralwidget)
    self.dot1.setGeometry(QtCore.QRect(850, 450, 1000, 150))
    self.dot1.setObjectName("info")
    self.dot1.setFont(QtGui.QFont("맑은 고딕",30))
    self.dot1.setStyleSheet("Color : white")

    self.dot2 = QtWidgets.QLabel(self.centralwidget)
    self.dot2.setGeometry(QtCore.QRect(900, 450, 1000, 150))
    self.dot2.setObjectName("info")
    self.dot2.setFont(QtGui.QFont("맑은 고딕",30))
    self.dot2.setStyleSheet("Color : white")

    self.dot3 = QtWidgets.QLabel(self.centralwidget)
    self.dot3.setGeometry(QtCore.QRect(950, 450, 1000, 150))
    self.dot3.setObjectName("info")
    self.dot3.setFont(QtGui.QFont("맑은 고딕",30))
    self.dot3.setStyleSheet("Color : white")

    photos.append(self.photo1)
    photos.append(self.photo2)
    photos.append(self.photo3)
    photos.append(self.photo4)

    dots.append(self.dot1)
    dots.append(self.dot2)
    dots.append(self.dot3)

def face_scan(self,MainWindow):
    text = "    - 커트 혹은 펌을 선택해 주세요 -"
    self.set_txt(text)
    kakao_voice(text)
    self.window_status = "init_hair"
    btn_control.init_hair_voice_info(self,MainWindow)

def start_camera(self,MainWindow,user_hair):
    if status_check() == 0:
        return

    self.window_status = "wait"
    self.user_hair = user_hair
    self.face_scan_timer = 600
    self.infomation_txt.setGeometry(QtCore.QRect(750, 420, 1000, 300))
    text = "     사진 촬영을 하겠습니다.\n       정면을 바라봐 주세요"
    self.set_txt(text)
    kakao_voice(text)

    self.camera_start(MainWindow)
    # for i in range(3,0,-1):
    #     self.camera_timer.setText(i)

    
def thread_camera(self,MainWindow):
    global photos,dots,return_hair_location

    info.wait_info_data(self,MainWindow)

    #hair_setting_send(self,MainWindow)
    
    self.camera_timer.show()
    for i in range(4,0,-1):
        self.camera_timer.setText(f"{i}")
        sleep(1)
    self.camera_timer.hide()


    self.set_txt("         사진 촬영중...")
    #pi_camera()
    #image_send(self,MainWindow)
    kakao_voice("얼굴 분석중 입니다. 잠시만 기달려 주세요")
    self.set_txt("         얼굴 분석 중")

    for i in dots:
        i.show()



    for time in range(6//3):
        for i in range(3):
            for x in dots:
                if x != dots[i]:
                    x.setText("●")
                    x.setStyleSheet("Color : white")
            dots[i].setStyleSheet("Color : green")     
            sleep(1)

    for i in dots:
        i.hide()

    self.set_txt("")
    
    kakao_voice("\
헤어 추천이 완료되었습니다. \
헤어스타일 안내가 필요하시면 \"설명해줘\" 라고 말씀해 주세요.\
처음으로 돌아가시려면 \"메인화면\" 이라고 말씀해 주세요.")

    self.infomation_txt.setGeometry(QtCore.QRect(750, 170, 1000, 300))
    num = 1
    for i in photos:
        file_name = "test" + f"{num}"
        pixmap = QtGui.QPixmap(f"{return_hair_location}{file_name}.jpg")
        pixmap = pixmap.scaledToWidth(450)
        i.setPixmap(QPixmap(pixmap))
        i.resize(450,450)
        i.show()
        num = num+1


    btn_control.end_hair_voice_info(self,MainWindow)
    self.window_status = "show_hair"