
from gui import info
from voice_control import kakao_voice

def main_page_voice_info(self,MainWindow):
    text_data = []
    text_data.append(["헤어스타일 추천", "머리 추천해줘"])
    text_data.append(["유행 머리 안내", "유행하는 머리 알려줘"])
    
    info.set_info_data(self,MainWindow,text_data)

def init_hair_voice_info(self,MainWindow):
    text_data = []
    text_data.append(["커트", "커트 해줘"])
    text_data.append(["펌", "펌 해줘"])
    text_data.append(["메인화면", "메인화면 돌아가줘"])
    
    info.set_info_data(self,MainWindow,text_data)

def end_hair_voice_info(self,MainWindow):
    text_data = []
    text_data.append(["메인화면", "메인화면 돌아가줘"])

    
    info.set_info_data(self,MainWindow,text_data)


def main_page_setting(self, MainWindow):
    text = "메인화면으로 돌아왔습니다.\n사용할 기능을 말씀해주세요"
    self.set_txt(text,1)
    kakao_voice(text)
    main_ui_reset(self, MainWindow)
    

def main_ui_reset(self, MainWindow):
    main_page_voice_info(self, MainWindow)
    self.window_status = "main"
    self.photo1.hide()
    self.photo2.hide()
    self.photo3.hide()
    self.photo4.hide()
    self.camera_timer.hide()