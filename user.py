from time import sleep
from gui import btn_control
now_stats = 0

def user_login(self,MainWindow):
    global now_stats

    while 1:
        if self.face_scan_enable == 1 and now_stats == 0:
            now_stats = 1
            
            self.user_name = "홍길동"
            self.user_phone = "01012345678"
            self.user_type = "men"


            txt = "            홍길동님 반갑습니다.\n오늘은 어떤 머리를 하러 오셨나요?"
            # kakao_voice(txt)
            self.voice_status_setting(txt,self.window_status)
            self.set_txt(txt,1)
            self.face_scan_enable = 0

        if now_stats == 1 and self.face_scan_timer > 0 :
            self.face_scan_timer = self.face_scan_timer -1
        
        elif now_stats == 1 and self.face_scan_timer == 0:
            self.face_scan_timer = -1
            now_stats = 0
            self.face_scan_enable = 0
            
            txt = "       자동 로그아웃 되었습니다."
            # kakao_voice(txt)
            self.voice_status_setting(txt,self.window_status)
            self.set_txt(txt,1)
            btn_control.main_ui_reset(self,MainWindow)

        #print(f"{now_stats}, {self.face_scan_timer}")
        sleep(0.1)
        

def status_check():
    global now_stats
    return now_stats