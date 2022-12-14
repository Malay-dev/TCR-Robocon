from Motor_Setup import *
import sys
sys.path.append("Motors")


kp = 15
kd = 20
ki = 0.02

priError = 0
toError = 0


def mapping(value, x, y, a, b):
    res = abs(b-a)/(y-x)
    return res*value


def PID(x):
    print("Aligning Aruco")
    global priError
    global toError
    if x != None:
        curr_x = x
        set_x = 0
        error = set_x - curr_x
        Pvalue = error * kp
        Ivalue = toError * ki
        Dvalue = (error - priError) * kd
        PIDvalue = Pvalue + Ivalue + Dvalue
        priError = error
        toError = error + toError
        print(PIDvalue)
        res_val = mapping(PIDvalue, 0, 135, 0, 100)
        if x > 0:
            # LEFT
            LEFT(res_val)
        elif x < 0:
            # RIGHT
            RIGHT(res_val)
        
        
