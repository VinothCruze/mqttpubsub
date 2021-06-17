import paho.mqtt.client as mqtt
import time

def on_log(client, userdata, level, buf):
    print("log: "+buf)

def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected flags"+"result code "+str(rc)+"client_id")
    client.connected_flag = False

def on_connect(client, userdata, flags, rc):

    #rc is the return code
    if rc == 0 :
        print("Successfully connected!")
        client.is_connected = True

    else:
        print("Error connecting:",rc)


def on_message(client,userdata,msg):
    topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8","ignore"))
    print("message received",m_decode)

broker = '192.168.0.111'
client = mqtt.Client("Python1")


client.on_connect = on_connect
client.on_disconnect = on_disconnect
#client.on_log= on_log #client logging
client.on_message = on_message

print('Connecting to broker', broker)

client.connect(broker)
client.loop_start() #start network loop
client.subscribe("house/sensor1")
client.publish("house/sensor1","my first message")


time.sleep(4)
client.loop_stop() #start network loop
client.disconnect()
