from time import sleep

import cv2
import time

# Explicitly open a new file called my_image.jpg

file_location = "temp/image/"



face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

def pi_camera():
    global cap,ret, frame

    print("start camera")
    now = time.localtime()

    ret, frame = cap.read() 
    cap.set(3,640) # 너비
    cap.set(4,480) # 높이
    file_name = f"{file_location}{now.tm_year}_{now.tm_mon}_{now.tm_mday}_{now.tm_hour}{now.tm_min}{now.tm_sec}.jpg"


    cv2.imwrite(f'{file_name}', frame) # 사진 저장
    print("end camera")



def user_face_scan(self,MainWindow):
    global cap,face_classifier

    if cap.isOpened():
        print('width: {}, height : {}'.format(cap.get(3), cap.get(4)))
    else:
        print("No Camera")


    try:

        while True:
            ret, frame = cap.read() 
            if ret:

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # 얼굴 검출
                faces = face_classifier.detectMultiScale(gray,1.3,5)
                
                for (x,y,w,h) in faces:
                    self.face_scan_enable = 1
                    self.face_scan_timer = 600
                    

                sleep(0.1)
                #cv2.imshow('video', frame)
            else:
                print('error')
                sleep(0.5)
            
    except:
        print("error")
        cap.release()
        cv2.destroyAllWindows()


def sys_end():
    global cap

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        user_face_scan()
    except:
        sys_end()