
from PyQt5 import QtCore, QtGui, QtWidgets #pip install pyqt5(pip install python3-pyqt5)
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPixmap, QFont, QFontDatabase
from PyQt5.QtCore import Qt
import time
import PIL
from PIL import Image,ImageDraw,ImageFont
import os
from gui import btn_control

def init_info(self,MainWindow):
    fontDB = QFontDatabase()
    fontDB.addApplicationFont('./font/Lobster-Regular.ttf')
    fontDB.addApplicationFont('./font/NanumGothic-Regular.ttf')
    
    #time 이라는 이름으로 label 생성 [(오전/오후)시/분]
    self.time = QtWidgets.QLabel(self.centralwidget)
    self.time.setGeometry(QtCore.QRect(1700,80,800,60))
    self.time.setObjectName("time")
    #setFont(QtGui.QFont("Font_name",Font_size))
    self.time.setFont(QtGui.QFont("NanumGothic",20)) 
    self.time.setStyleSheet("Color : white")

    #date 이라는 이름으로 label 생성 [년/월/일]
    self.date = QtWidgets.QLabel(self.centralwidget)
    self.date.setGeometry(QtCore.QRect(1700, 15, 300, 50))
    self.date.setObjectName("date")
    self.date.setFont(QtGui.QFont("NanumGothic",20))
    self.date.setStyleSheet("Color : white")

    #title
    self.title = QtWidgets.QLabel(self.centralwidget)
    self.title.setGeometry(QtCore.QRect(670, 20, 1000, 150))
    self.title.setObjectName("title")
    self.title.setFont(QtGui.QFont("Lobster",80))
    self.title.setStyleSheet("Color : white")
    self.title.setText("Frisör. Faszination")

    self.infomation_txt = QtWidgets.QLabel(self.centralwidget)
    self.infomation_txt.setGeometry(QtCore.QRect(750, 170, 1000, 300))
    self.infomation_txt.setObjectName("info")
    self.infomation_txt.setFont(QtGui.QFont("NanumGothic",25))
    self.infomation_txt.setAlignment(Qt.AlignLeft)
    self.infomation_txt.setStyleSheet("Color : white")

    self.voice_info = QtWidgets.QLabel(self.centralwidget)
    self.voice_info.setGeometry(QtCore.QRect(50, 100, 500, 800))
    self.voice_info.setObjectName("info")
    self.voice_info.setFont(QtGui.QFont("NanumGothic",20))
    self.voice_info.setAlignment(Qt.AlignLeft)
    self.voice_info.setStyleSheet("Color : white")

    #image
    self.back_img1 = QtWidgets.QLabel(self.centralwidget)
    self.back_img1.setGeometry(QtCore.QRect(0,541,10,60))
    pixmap = QtGui.QPixmap(f"./font/1.jpg")
    self.back_img1.setPixmap(QPixmap(pixmap))
    self.back_img1.resize(450,539)
    self.back_img1.show()

    self.back_img2 = QtWidgets.QLabel(self.centralwidget)
    self.back_img2.setGeometry(QtCore.QRect(1470,592,10,60))
    pixmap = QtGui.QPixmap(f"./font/2.jpg")
    pixmap = pixmap.scaledToWidth(450)
    self.back_img2.setPixmap(QPixmap(pixmap))
    self.back_img2.resize(450,488)
    self.back_img2.show()
    
    btn_control.main_page_voice_info(self,MainWindow)


def set_info_data(self,MainWindow,data):

    text = f"\
    음성 인식 안내\n\n\n"

    for i in data:
        text = text + f"  * {i[0]}\n\
          \"{i[1]}\"\n\n"


    self.voice_info.setText(text)

def wait_info_data(self,MainWindow):
    self.voice_info.setText("\
    음성 인식 일시정지")


def txt_print(self,MainWindow):

    while(1):
        self.infomation_txt.setText(self.info_data)
        if self.txt_timer > 0:
            self.txt_timer = self.txt_timer - 1

        elif self.txt_timer == 0:
            self.txt_timer = -1
            self.info_data = ""

        time.sleep(0.2)