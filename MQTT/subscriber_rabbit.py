import paho.mqtt.client as mqtt
import cv2
import sys
sys.path.append("Motors")
from Motor_Setup import *
sys.path.append("Aruco")
from Detect_Aruco import ID, DISTANCE, CO_ORDINATES, ANGLE, findAruco, distance_pose
from Align_Aruco import PID

    
    elif(input == "ALIGN_RABBIT"):
        VideoCap = True
        capture = cv2.VideoCapture(0)
        while True:
            if VideoCap:
                _, frame = capture.read()
                # frame = cv2.resize(frame, (0, 0), fx=0.7, fy=0.7)
                ARUCO_DICT, ARUCO_PARAMS = findAruco(frame)
                distance_pose(frame, ARUCO_DICT=ARUCO_DICT, ARUCO_PARAMS=ARUCO_PARAMS)
                if ID() > -1:
                    a=ANGLE()
                    PID(a)
                cv2.imshow("input2", frame)
                if cv2.waitKey(1) == 113:
                    break
        cv2.destroyAllWindows()