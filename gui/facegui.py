from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets #pip install pyqt5(pip install python3-pyqt5)
from image import pi_camera
from mqtt_client import image_send,hair_setting_send
from picamera import PiCamera
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QPushButton
from gui import btn_control, info
from PIL import Image,ImageDraw,ImageFont
import mqtt_client
import sys
import os

from user import status_check
fontsFolder = './font'    #글자로 쓸 폰트 경로
return_hair_location = "./temp/return_image/"

hair_data = {
    'person_type' : '',
    'hair_type' : ''
}

photos = []


image_choice_num = 0

json_save = {}

def init_hair_gui(self,MainWindow):
    global photos

    self.camera_timer = QtWidgets.QLabel(self.centralwidget)
    self.camera_timer.setGeometry(QtCore.QRect(850, 500, 1000, 150))
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


    photos.append(self.photo1)
    photos.append(self.photo2)
    photos.append(self.photo3)
    photos.append(self.photo4)



    self.face_type = QtWidgets.QLabel(self.centralwidget)
    self.face_type.setGeometry(QtCore.QRect(1500, 200, 1000, 150))
    self.face_type.setObjectName("info")
    self.face_type.setFont(QtGui.QFont("맑은 고딕",20))
    self.face_type.setStyleSheet("Color : white")


def json_val_save(json_val):
    global json_save
    json_save = json_val
    print(json_save)



def face_scan(self,MainWindow):
    global json_save
    json_save = {}

    text = "    - 커트 혹은 펌을 선택해 주세요 -"
    self.set_txt(text)
    # kakao_voice(text)
    # self.window_status = "init_hair"
    self.voice_status_setting(text,"init_hair")
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
    # kakao_voice(text)
    self.voice_status_setting(text,"wait")
    self.camera_start(MainWindow)
    # for i in range(3,0,-1):
    #     self.camera_timer.setText(i)

    
def thread_camera(self,MainWindow):
    global photos,return_hair_location,image_choice_num, json_save

    info.wait_info_data(self,MainWindow)

    hair_setting_send(self,MainWindow)
    self.mqtt_status = 1
    self.mqtt_recv_end = 0
    self.video_stop == 1

    self.camera_timer.show()
    for i in range(4,0,-1):
        self.camera_timer.setText(f"    {i}")
        sleep(1)
    self.camera_timer.hide()


    self.set_txt("         사진 촬영중...")
    pi_camera()
    image_send(self,MainWindow)
    

    text = "얼굴 분석중 입니다. 잠시만 기달려 주세요"

    self.voice_status_setting(text,"wait")
    self.set_txt("         얼굴 분석 중...")

    self.camera_timer.show()

    for i in range(1):
        self.camera_timer.setText(f"{i+1}/10")      
        sleep(1)
        
        if self.mqtt_recv_end == 1:
            break
    
    self.camera_timer.hide()

    self.mqtt_recv_end = 0
    self.mqtt_status = 0    
    self.video_stop == 0

        

    # if json_save == {}:
    if json_save != {}:
        self.face_type.setText(f"\
{self.user_name}님의 얼굴형\n\
     - {json_save['face_shape']}\n\
{self.user_name}님의 현재 헤어스타일\n\
     - {json_save['before_hair']}")

        self.face_type.show()



        self.set_txt("")
        text = "\
    헤어 추천이 완료되었습니다. \
    미용하실 헤어스타일의 번호를 말씀해 주세요.\
    헤어스타일 안내가 필요하시면 \"설명해줘\" 라고 말씀해 주세요.\
    처음으로 돌아가시려면 \"메인화면\" 이라고 말씀해 주세요."


        self.voice_status_setting(text,"show_hair")
        sleep(0.3)
        self.infomation_txt.setGeometry(QtCore.QRect(750, 170, 1000, 300))

        image_numbering()

        num = 1
        for i in photos:
            file_name = "test" + f"{num}"
            pixmap = QtGui.QPixmap(f"{return_hair_location}{file_name}.jpg")
            pixmap = pixmap.scaledToWidth(450)
            i.setPixmap(QPixmap(pixmap))
            i.resize(450,450)
            i.show()
            num = num+1
            sleep(0.01)

        image_choice_num = 0
        btn_control.end_hair_voice_info(self,MainWindow)

    else : 
        txt = "서버와 연결 실패했습니다.\n직원에게 문의해주세요"
        self.set_txt(txt,1)
        self.voice_status_setting(txt,"main")
        btn_control.main_ui_reset(self,MainWindow)

        pass

    sys.exit(0)




def image_numbering():

    global return_hair_location, fontsFolder

    x = 1
    for i in range(4) :
        file_name = "test" + f"{x}"
        target_image = Image.open(f'{return_hair_location}{file_name}.jpg')  #일단 기본배경폼 이미지를 open 합니다.
        selectedFont =ImageFont.truetype(os.path.join(fontsFolder,'font.ttf'),50) #폰트경로과 사이즈를 설정해줍니다.
        draw =ImageDraw.Draw(target_image)

        draw.text((20,400),f'{x}',fill="yellow",font=selectedFont,align='center') # fill= 속성은 무슨 색으로 채울지 설정,font=는 자신이 설정한 폰트 설정

        x = x+1

        test = target_image.convert('RGB')

        test.save(f"{return_hair_location}{file_name}.jpg") #편집된 이미지를 저장합니다.

        target_image.close()

def image_choice(self,MainWindow,number):
    global return_hair_location, fontsFolder,photos,image_choice_num

    file_name = "test" + f"{number}"
    target_image = Image.open(f'{return_hair_location}{file_name}.jpg')  #일단 기본배경폼 이미지를 open 합니다.
    selectedFont =ImageFont.truetype(os.path.join(fontsFolder,'font.ttf'),50) #폰트경로과 사이즈를 설정해줍니다.
    draw =ImageDraw.Draw(target_image)

    draw.line((0, 0, 0, 458), fill="yellow", width=7)
    draw.line((0, 458, 460, 458), fill="yellow", width=7)
    draw.line((460, 0, 460, 458), fill="yellow", width=7)
    draw.line((0, 0, 460, 0), fill="yellow", width=7)


    test = target_image.convert('RGB')

    test.save(f"{return_hair_location}choice.jpg") #편집된 이미지를 저장합니다.

    target_image.close()

    sleep(0.01)

    pixmap = QtGui.QPixmap(f"{return_hair_location}choice.jpg")
    pixmap = pixmap.scaledToWidth(450)
    photos[number-1].setPixmap(QPixmap(pixmap))
    photos[number-1].resize(450,450)
    photos[number-1].show()
    sleep(0.01)

    image_choice_num = number

    text = f"{number}번을 선택하셨습니다. 맞으면 확인, 다르면 취소라 말씀해 주세요."
    self.voice_status_setting(text,"choice_hair")

    btn_control.choice_num_check(self,MainWindow)

def cancel_choice(self,MainWindow):
    global image_choice_num

    pixmap = QtGui.QPixmap(f"{return_hair_location}test{image_choice_num}.jpg")
    pixmap = pixmap.scaledToWidth(450)
    photos[image_choice_num-1].setPixmap(QPixmap(pixmap))
    photos[image_choice_num-1].resize(450,450)
    photos[image_choice_num-1].show()
    sleep(0.01)

    text = f"취소했습니다. 다른 번호를 선택하시거나 기능을 말씀해 주세요."
    self.voice_status_setting(text,"show_hair")
    image_choice_num = 0
    btn_control.end_hair_voice_info(self,MainWindow)

def ckeck_choice(self,MainWindow):
    global image_choice_num,photos
    
    for i in photos:
        i.hide()
        sleep(0.01)

    text = f"                미용을 시작하겠습니다.\n미용이 끝나시면 '계산' 혹은 '종료'라고 말씀해 주세요."
    self.set_txt(text,1)
    self.voice_status_setting(text,"start_hair")
    image_choice_num = 0
    btn_control.start_hair(self,MainWindow)
    
def end_hair(self,MainWindow):
    text = f"미용이 종료되었습니다.\n 즐거운 하루 보내세요."
    self.set_txt(text,1)
    self.voice_status_setting(text,"main")

    btn_control.main_page_voice_info(self,MainWindow)