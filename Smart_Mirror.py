# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets #pip install pyqt5(pip install python3-pyqt5)


from time import sleep
import threading
import tkinter as tk #this can't pip install


from PyQt5.QtWidgets import QPushButton

from PIL import Image
import numpy as np
from gui import facegui,setupgui, timegui, info, btn_control
import voice_control, image, user

from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

#==================================================================================================
#==============UI_MAIN==============================================================================
#==================================================================================================



class Ui_MainWindow(object):
    hello_world = 0
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    start_or_stop=False
    start=True

    face_scan_enable = 0
    face_scan_timer = -1

    # user_name = "None"
    # user_phone = "None"
    # user_type = "None"
    # user_hair = ""

    user_name = "홍길동"
    user_phone = "01012345678"
    user_type = "men"
    user_hair = ""

    window_status = "main"
    voice_onoff_status = 0
    voice_txt = ""

    info_data = ""
    txt_timer = -1

    def setupUi(self, MainWindow):
        setupgui.setupUi(self, MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SmartMirror"))
        
    #-----------------------------------------------------------------------------------------
    # 이벤트
    # EVENT
    #-----------------------------------------------------------------------------------------
    def txt_print(self,MainWindow):
        info.txt_print(self,MainWindow)
        pass
    def set_txt(self,data,timer = 0):
        if timer == 0:
            self.txt_timer = -1
            self.info_data = f"{data}"
        elif timer == 1:
            self.txt_timer = 5*5
            self.info_data = f"{data}"

    
    def cam_start(self,MainWindow):
        print("커트 중간")
        facegui.thread_camera(self,MainWindow)




    
    #시간을 알려주는 함수 메인 화면에 생성
    # now.(year,month,day,hour,minute,second)
    def set_time(self,MainWindow):
        timegui.set_time(self,MainWindow)

    #음성인식 실행
    def voice_scan(self,MainWindow):
        voice_control.voice_scan(self,MainWindow)
    #음성 안내 실행
    def voice_start(self,MainWindow):
        voice_control.kakao_voice(self.voice_txt)
    #안면인식
    def face_scan(self,MainWindow):
        image.user_face_scan(self,MainWindow)
    def auto_user_login(self,MainWindow):
        user.user_login(self,MainWindow)


    def voice_status_setting(self,voice_txt,window_status):
        self.voice_txt = voice_txt
        self.window_status = window_status
        self.sound_start(MainWindow)

 
    #----------------------------------------------------------------------------------------------------
    #------------------------ 쓰레드 ---------------------------------------------------------------------
    #----------------------------------------------------------------------------------------------------

    #Set_time을 쓰레드로 사용
    def time_start(self,MainWindow):
        thread=threading.Thread(target=self.set_time,args=(self,))
        thread.daemon=True #프로그램 종료시 프로세스도 함께 종료 (백그라운드 재생 X)
        thread.start()

    def camera_start(self,MainWindow):
        thread=threading.Thread(target=self.cam_start,args=(self,))
        thread.daemon=True #프로그램 종료시 프로세스도 함께 종료 (백그라운드 재생 X)
        thread.start()

    def txt_output(self,MainWindow):
        thread=threading.Thread(target=self.txt_print,args=(self,))
        thread.daemon=True #프로그램 종료시 프로세스도 함께 종료 (백그라운드 재생 X)
        thread.start()
    
    def mic_start(self,MainWindow):
        thread=threading.Thread(target=self.voice_scan,args=(self,))
        thread.daemon=True #프로그램 종료시 프로세스도 함께 종료 (백그라운드 재생 X)
        thread.start()

    def sound_start(self,MainWindow):
        thread=threading.Thread(target=self.voice_start,args=(self,))
        thread.daemon=True #프로그램 종료시 프로세스도 함께 종료 (백그라운드 재생 X)
        thread.start()

    def user_scan(self,MainWindow):
        thread=threading.Thread(target=self.face_scan,args=(self,))
        thread.daemon=True #프로그램 종료시 프로세스도 함께 종료 (백그라운드 재생 X)
        thread.start()

    def login_timer(self,MainWindow):
        thread=threading.Thread(target=self.auto_user_login,args=(self,))
        thread.daemon=True #프로그램 종료시 프로세스도 함께 종료 (백그라운드 재생 X)
        thread.start()


#-------------메인---------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)
    # ui.button(MainWindow)

    ui.time_start(MainWindow) #time thread
    ui.txt_output(MainWindow)
    ui.mic_start(MainWindow)
    ui.user_scan(MainWindow)
    ui.login_timer(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())