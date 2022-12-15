import paho.mqtt.client as mqtt
import cv2
import sys
sys.path.append("Motors")
from Motor_Setup_Rabbit import *


def control_bot(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))
    Recieve = str(message.payload.decode("utf-8")).split("-")
    input = Recieve[0]
    if(len(Recieve)>1):
        pwmval = int(Recieve[1])
    if(input == "FORWARD"):
        FORWARD(pwmval)
    elif(input == "BACKWARD"):
        BACKWARD(pwmval)
    elif(input == "RIGHT"):
        RIGHT(pwmval)
    elif(input == "LEFT"):
        LEFT(pwmval)
    elif(input == "FORWARD_LEFT_DIAGONAL"):
        FORWARD_LEFT_DIAGONAL(pwmval)
    elif(input == "FORWARD_RIGHT_DIAGONAL"):
        FORWARD_RIGHT_DIAGONAL(pwmval)
    elif(input == "BACKWARD_LEFT_DIAGONAL"):
        BACKWARD_LEFT_DIAGONAL(pwmval)
    elif(input == "ROTATE_LEFT"):
        ROTATE_LEFT(pwmval)
    elif(input == "ROTATE_RIGHT"):
        ROTATE_RIGHT(pwmval)
    elif(input == "STOP"):
        STOP()
    
        

client_id = "RASPI_2"
port = 1883
broker = "localhost"  # or IP address

client = mqtt.Client(client_id)
if client.connect(broker, port) != 0:
    print("Could not connect to client")
    sys.exit(-1)

client.subscribe("CONTROLLER_INPUTS_RABBIT")
client.on_message = control_bot
client.loop_forever()