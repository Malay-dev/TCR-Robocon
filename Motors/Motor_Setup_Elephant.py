import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# MOTOR-1 LEFT
AN1 = 15
DIG1 = 14
# MOTOR-2 LEFT
AN2 = 4
DIG2 = 18
# MOTOR-3 RIGHT
AN3 = 27
DIG3 = 17
# MOTOR-4 RIGHT
AN4 = 23
DIG4 = 22

# MOTOR SETUP 
GPIO.setup(AN1, GPIO.OUT)
GPIO.setup(DIG1, GPIO.OUT)
GPIO.setup(AN2, GPIO.OUT)
GPIO.setup(DIG2, GPIO.OUT)
GPIO.setup(AN3, GPIO.OUT)
GPIO.setup(DIG3, GPIO.OUT)
GPIO.setup(AN3, GPIO.OUT)
GPIO.setup(DIG3, GPIO.OUT)

p1 = GPIO.PWM(AN1, 100)			# set pwm for M1
p2 = GPIO.PWM(AN2, 100)			# set pwm for M2
p3 = GPIO.PWM(AN3, 100)			# set pwm for M3
p4 = GPIO.PWM(AN4, 100)			# set pwm for M4

# "" INITAL VALUE -- STOP ""
GPIO.output(DIG1, GPIO.LOW)          # Direction can ignore
GPIO.output(DIG2, GPIO.LOW)          # Direction can ignore
GPIO.output(DIG3, GPIO.LOW)          # Direction can ignore
GPIO.output(DIG4, GPIO.LOW)          # Direction can ignore
p1.start(0)                          # set speed for M1 at 0%
p2.start(0)
p3.start(0)
p4.start(0)



def FORWARD(pwm_value):
    print("move forward")
    GPIO.output(DIG1, GPIO.HIGH)
    GPIO.output(DIG2, GPIO.HIGH)
    GPIO.output(DIG3, GPIO.HIGH)
    GPIO.output(DIG4, GPIO.HIGH)
    p1.start(pwm_value)
    p2.start(pwm_value)
    p3.start(pwm_value)
    p4.start(pwm_value)


def BACKWARD(pwm_value):
    print("move backward")
    GPIO.output(DIG1, GPIO.LOW)
    GPIO.output(DIG2, GPIO.LOW)
    GPIO.output(DIG3, GPIO.LOW)
    GPIO.output(DIG4, GPIO.LOW)
    p1.start(pwm_value)
    p2.start(pwm_value)
    p3.start(pwm_value)
    p4.start(pwm_value)


def LEFT(pwm_value):
    print("move left")
    GPIO.output(DIG1, GPIO.HIGH)
    GPIO.output(DIG2, GPIO.LOW)
    GPIO.output(DIG3, GPIO.LOW)
    GPIO.output(DIG4, GPIO.HIGH)
    p1.start(pwm_value)
    p2.start(pwm_value)
    p3.start(pwm_value)
    p4.start(pwm_value)


def RIGHT(pwm_value):
    print("move right")
    GPIO.output(DIG1, GPIO.LOW)
    GPIO.output(DIG2, GPIO.HIGH)
    GPIO.output(DIG3, GPIO.HIGH)
    GPIO.output(DIG4, GPIO.LOW)
    p1.start(pwm_value)
    p2.start(pwm_value)
    p3.start(pwm_value)
    p4.start(pwm_value)


def LEFT_FORWARD_DIAGONAL(pwm_value):
    print("move lfd")
    GPIO.output(DIG1, GPIO.HIGH)
    GPIO.output(DIG2, GPIO.HIGH)
    GPIO.output(DIG3, GPIO.HIGH)
    GPIO.output(DIG4, GPIO.HIGH)
    p1.start(0)
    p2.start(pwm_value)
    p3.start(pwm_value)
    p4.start(0)


def RIGHT_FORWARD_DIAGONAL(pwm_value):
    print("move rfd")
    GPIO.output(DIG1, GPIO.HIGH)
    GPIO.output(DIG2, GPIO.HIGH)
    GPIO.output(DIG3, GPIO.HIGH)
    GPIO.output(DIG4, GPIO.HIGH)
    p1.start(pwm_value)
    p2.start(0)
    p3.start(0)
    p4.start(pwm_value)


def LEFT_BACKWARD_DIAGONAL(pwm_value):
    print("move lbd")
    GPIO.output(DIG1, GPIO.LOW)
    GPIO.output(DIG2, GPIO.LOW)
    GPIO.output(DIG3, GPIO.LOW)
    GPIO.output(DIG4, GPIO.LOW)
    p1.start(0)
    p2.start(pwm_value)
    p3.start(pwm_value)
    p4.start(0)


def RIGHT_BACKWARD_DIAGONAL(pwm_value):
    print("move rbd")
    GPIO.output(DIG1, GPIO.LOW)
    GPIO.output(DIG2, GPIO.LOW)
    GPIO.output(DIG3, GPIO.LOW)
    GPIO.output(DIG4, GPIO.LOW)
    p1.start(pwm_value)
    p2.start(0)
    p3.start(0)
    p4.start(pwm_value)


def STOP():
    print("Stop")
    GPIO.output(DIG1, GPIO.LOW)
    GPIO.output(DIG2, GPIO.LOW)
    GPIO.output(DIG3, GPIO.LOW)
    GPIO.output(DIG4, GPIO.LOW)
    p1.start(0)
    p2.start(0)
    p3.start(0)
    p4.start(0)


def ROTATE_LEFT(pwm_value):
    print("Rotate left")
    GPIO.output(DIG1, GPIO.LOW)
    GPIO.output(DIG2, GPIO.LOW)
    GPIO.output(DIG3, GPIO.HIGH)
    GPIO.output(DIG4, GPIO.HIGH)
    p1.start(pwm_value)
    p2.start(pwm_value)
    p3.start(pwm_value)
    p4.start(pwm_value)


def ROTATE_RIGHT(pwm_value):
    print("Rotate right")
    GPIO.output(DIG1, GPIO.HIGH)
    GPIO.output(DIG2, GPIO.HIGH)
    GPIO.output(DIG3, GPIO.LOW)
    GPIO.output(DIG4, GPIO.LOW)
    p1.start(pwm_value)
    p2.start(pwm_value)
    p3.start(pwm_value)
    p4.start(pwm_value)
