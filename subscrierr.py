import paho.mqtt.client as mqtt

# when 1st message is received print it, disconnect and exit the program
def on_message(client, userdata, message):
    client.message_received = True
    print('Received message')
    print('message:', str(message.payload.decode('UTF-8')))
    print('Disconnecting now')
    client.loop_stop()
    client.disconnect()
    exit(0)

# when subscibtion is successful, acknowledge it 
def on_subscribe(client, userdata, mid, granted_qos):
    print('Subscribed to house/bulb1')
    return

broker = '192.168.0.111' # Broker's IP address
port = '' # Broker's port address (not necessary as defaults to 1883)

# creating a class member flag to indicate if a message is received or not
mqtt.Client.message_received = False

# defining the client object and the required callbacks
client = mqtt.Client('Python-Subscriber')
client.on_subscribe = on_subscribe
client.on_message = on_message


# connect and subscribe
try:

    client.connect(broker)
    ret, mid = client.subscribe('house/bulb1', 1)

    if not ret == 0:
        print('Could not subscribe')

    client.loop_start() # start a loop to handle callbacks and connection in another thread

    while client.message_received == False:
        #do nothing and just wait to keep the progran running long enough for the first message to be received
        pass

# if exception occurs
except:
    print('could not connect')
    exit(1)
