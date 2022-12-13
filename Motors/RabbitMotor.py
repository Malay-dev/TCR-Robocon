import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
AN2 = 11
AN1 = 8
DIG2 = 25
DIG1 = 7

GPIO.setup(AN2, GPIO.OUT)
GPIO.setup(AN1, GPIO.OUT)
GPIO.setup(DIG2, GPIO.OUT)
GPIO.setup(DIG1, GPIO.OUT)		# delay for 1 seconds

p1 = GPIO.PWM(AN1, 50)			# set pwm for M1
p2 = GPIO.PWM(AN2, 50)			# set pwm for M2

GPIO.output(DIG1, GPIO.LOW)          # Direction can ignore
GPIO.output(DIG2, GPIO.LOW)          # Direction can ignore
p1.start(0)                          # set speed for M1 at 0%
p2.start(0)

# Functions for Control for Each Wheel- can be called as needed Universally


def rforward():
    GPIO.output(DIG1, GPIO.HIGH)
    p1.start(25)


def rback():
    GPIO.output(DIG1, GPIO.LOW)
    p1.start(25)


def lforward():
    GPIO.output(DIG2, GPIO.LOW)
    p2.start(25)


def lback():
    GPIO.output(DIG2, GPIO.HIGH)
    p2.start(25)


def rlstop():
    p1.start(0)
    p2.start(0)

# Rabbit Rotations FUNCTIONs


def rabbitRotateL():
    rforward()  # GPIO.output(DIG1, GPIO.HIGH)
    lback()  # GPIO.output(DIG2, GPIO.HIGH)


def rabbitRotateR():
    lforward()  # GPIO.output(DIG1, GPIO.LOW)
    rback()  # GPIO.output(DIG2, GPIO.LOW)


def on_message(client, userdata, message):
    inp = str(message.payload.decode("utf-8"))
    print(inp)
    if inp == "STOP":
        rlstop()

    elif inp == "BACKWARDS":
        rback()  # GPIO.output(DIG1, GPIO.LOW)
        lback()  # GPIO.output(DIG2, GPIO.HIGH)

    elif inp == "FORWARD":
        rforward()  # GPIO.output(DIG1, GPIO.HIGH)
        lforward()  # GPIO.output(DIG2, GPIO.LOW)

    elif inp == "RIGHT":
        rabbitRotateR()

    elif inp == "LEFT":
        rabbitRotateL()


mqttBroker = "192.168.140.71"
client = mqtt.Client("Controller_Subscriber")
client.connect(mqttBroker)


client.subscribe("Controller")
# speed control try
client.subscribe("Speed")


client.on_message = on_message
client.loop_forever()
