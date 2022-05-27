import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time




client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))


def on_subscribe(client, userdata, mid, granted_qos):
    #print("subscribed: " + str(mid) + " " + str(granted_qos))
    pass

def on_message(client, userdata, msg):
    try:
        message = str(msg.payload.decode("utf-8"))
        print(message)
    except:
        print("message error")

    





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
