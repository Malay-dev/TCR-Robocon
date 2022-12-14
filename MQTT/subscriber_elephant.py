import paho.mqtt.client as mqtt
import cv2
import sys
sys.path.append("Motors")
from Motor_Setup_Elephant import *
sys.path.append("Aruco")
from Detect_Aruco import ID, DISTANCE, CO_ORDINATES, ANGLE, findAruco, distance_pose
from Align_Aruco_Elephant import PID

def control_bot(client,userdata,message):
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
    elif(input == "ALIGN_ARUCO_ELEPHANT"):
        VideoCap = True
        capture = cv2.VideoCapture(0)
        while True:
            if VideoCap:
                flag = 0
                _, frame = capture.read()
                # frame = cv2.resize(frame, (0, 0), fx=0.7, fy=0.7)
                ARUCO_DICT, ARUCO_PARAMS, flag = findAruco(frame)
                distance_pose(frame, ARUCO_DICT=ARUCO_DICT, ARUCO_PARAMS=ARUCO_PARAMS)
                if ID() == 44 and flag == 1:
                    x,y = CO_ORDINATES()
                    PID(x)
                elif flag == 0:
                    STOP()
                cv2.imshow("Elephant_Feed", frame)
                if cv2.waitKey(1) == 113:
                    client.on_message = control_bot     
                    break               
        cv2.destroyAllWindows()
        


client_id = "RASPI_1"
port = 1883
broker = "localhost"  # or IP address

client = mqtt.Client(client_id)
if client.connect(broker, port) != 0:
    print("Could not connect to client")
    sys.exit(-1)

client.subscribe("CONTROLLER_INPUTS_ELEPHANT")
client.on_message = control_bot
client.loop_forever()
