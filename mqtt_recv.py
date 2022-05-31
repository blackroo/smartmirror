import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
from time import sleep
import json


status = 0
photo_num = 1
recv_end = 0

photo_save_location = "./temp/return_image/"

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("mirror image client OK")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))


def on_subscribe(client, userdata, mid, granted_qos):
    #print("subscribed: " + str(mid) + " " + str(granted_qos))
    pass

def on_message(client, userdata, msg):
    global status, photo_num, photo_save_location, recv_end

    if status == 1:
        try:
            check = str(msg.payload.decode("utf-8"))
            try:
                d = json.loads(msg.payload)
                print(d['success'])
            except:
                print("message error1")
                print("error: "+check)
                print()

        except:
            try:
                f = open(f"{photo_save_location}test{photo_num}", "wb")
                f.write(msg.payload)
                print("Image Received")
                f.close()
                photo_num = photo_num + 1

                if photo_num>=5 : 
                    photo_num = 1
                    recv_end = 1
            except:
                print("message error2")

    
def recv_status_check(self,MainWindow):
    global status, recv_end, photo_num
    while 1: 
        status = self.mqtt_status
        if recv_end == 1:
            self.mqtt_recv_end = 1
            recv_end = 0
        if status == 0:
            photo_num = 1
        sleep(0.2)





# 새로운 클라이언트 생성

# 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_subscribe(topic 구독),
# on_message(발행된 메세지가 들어왔을 때)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_message = on_message
# address : localhost, port: 1883 에 연결
try:
    client.connect('54.150.133.192', 1883)
    client.subscribe('Mirror', 1)
    client.loop_start()


except:
    print("connect fail")
