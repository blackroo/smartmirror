from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets #pip install pyqt5(pip install python3-pyqt5)
from mqtt_client import image_send,hair_setting_send
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QPushButton
from gui import btn_control, info
import mqtt_client
import sys
from user import status_check

people_type = ""
chart_img_location = "./temp/trend_chart/"

def init_trend(self, MainWindow):
    self.chart_img = QtWidgets.QLabel(self.centralwidget)
    self.chart_img.setGeometry(QtCore.QRect(700,250,10,60))
    self.chart_img.resize(0,0)

def start_trend(self, MainWindow):
    text = " - 추천받을 헤어스타일의 성별을 말씀해주세요 -"
    self.set_txt(text)

    self.voice_status_setting(text,"init_trand")

    btn_control.init_hair_trend(self, MainWindow)
    pass

def select_trend(self, MainWindow, type_set):
    global people_type
    people_type = type_set
    
    self.trend_thread(MainWindow)


def trend_hair(self,MainWindow):
    global people_type, chart_img_location

    self.set_txt("")
    text = "\
현재 유행하는 남성 헤어스타일 그래프입니다.\
1위는 댄디컷, 2위는 쉐도우펌, 3위는 가르마 컷입니다.\
다시 들으시려면 \"다시 말해줘\". \
헤어스타일 사진을 보고 싶으면 \"사진 보여줘\".\
처음으로 가시려면 \"메인화면\"이라고 말씀해주세요."


    self.voice_status_setting(text,"end_trend")



    file_name = f"{chart_img_location}{people_type}"
    pixmap = QtGui.QPixmap(f"{file_name}.jpg")
    pixmap = pixmap.scaledToWidth(650)
    self.chart_img.setPixmap(QPixmap(pixmap))
    self.chart_img.resize(650,650)
    self.chart_img.show()

    sleep(0.01)

    # 메인 화면으로 돌아가기
    btn_control.end_trend_info(self,MainWindow)

    sys.exit(0)

