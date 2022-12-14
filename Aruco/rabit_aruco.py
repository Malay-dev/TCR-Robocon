import sys
sys.path.append("Motors")
from RabbitMotor import *

kp = 15
kd = 20
ki = 0.02

priError = 0
toError = 0


def mapping(value, x, y, a, b):
    res = abs(b-a)/(y-x)
    return res*value


def PID_rabbit(x):
    print("Aligning rabbit")
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
        res_val = mapping(PIDvalue, 0, 60, 0, 100)
        if PIDvalue > 0:
            # LEFT
            rabitRotateL(res_val)
        elif PIDvalue < 0:
            # RIGHT
            rabitRotateR(res_val)
        else:
            rlstop()
