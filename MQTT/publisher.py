
import paho.mqtt.client as mqtt
import pygame

pygame.init()
# window = pygame.display.set_mode((200, 200))

joystick = pygame.joystick.Joystick(0)
joystick.init()


def throttle(value):
    value = abs(value)
    return int(75*value)


def Controller_Elephant():
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.JOYBUTTONDOWN:
                if pygame.joystick.Joystick(0).get_button(5):
                    return "ALIGN_ARUCO_ELEPHANT"
                if pygame.joystick.Joystick(0).get_button(6):
                    return "STOP_EVENT"
                if pygame.joystick.Joystick(0).get_button(7):
                    return "STOP-0"
            if event.type == pygame.JOYAXISMOTION:
                AXIS_0 = pygame.joystick.Joystick(0).get_axis(0)
                # Left - Right
                AXIS_1 = pygame.joystick.Joystick(0).get_axis(1)
                # Forward - Backward
                AXIS_4 = pygame.joystick.Joystick(0).get_axis(4)
                # Rotate Left
                AXIS_5 = pygame.joystick.Joystick(0).get_axis(5)
                # Rotate Right
                if event.__dict__.get("axis") == 1:
                    if AXIS_1 < 0 and AXIS_1 >= -1:
                        return "FORWARD-" + str(throttle(AXIS_1))
                    else:
                        return "BACKWARD-" + str(throttle(AXIS_1))
                elif event.__dict__.get("axis") == 0:
                    if AXIS_0 < 0 and AXIS_0 >= -1:
                        return "LEFT-" + str(throttle(AXIS_0))
                    else:
                        return "RIGHT-" + str(throttle(AXIS_0))
                elif round(AXIS_4) == -1 and round(AXIS_5) == -1:
                    return "STOP-0"
                elif event.__dict__.get("axis") == 4:
                    return "ROTATE_LEFT-" + str(throttle(AXIS_4))
                elif event.__dict__.get("axis") == 5:
                    return "ROTATE_RIGHT-" + str(throttle(AXIS_5))
                else:
                    return "STOP-"+"0"
            return 0

# def Controller_Rabbit():
#     while True:
#         for event in pygame.event.get():
#             print(event)
#             if event.type == pygame.JOYBUTTONDOWN:
#                 if pygame.joystick.Joystick(0).get_button(5):
#                     return "ALIGN_ARUCO_ELEPHANT"
#                 if pygame.joystick.Joystick(0).get_button(6):
#                     return "STOP_EVENT"
#                 if pygame.joystick.Joystick(0).get_button(7):
#                     return "STOP-0"
#             if event.type == pygame.JOYAXISMOTION:
#                 AXIS_0 = pygame.joystick.Joystick(0).get_axis(0)
#                 # Left - Right
#                 AXIS_1 = pygame.joystick.Joystick(0).get_axis(1)
#                 # Forward - Backward
#                 AXIS_4 = pygame.joystick.Joystick(0).get_axis(4)
#                 # Rotate Left
#                 AXIS_5 = pygame.joystick.Joystick(0).get_axis(5)
#                 # Rotate Right
#                 if event.__dict__.get("axis") == 1:
#                     if AXIS_1 < 0 and AXIS_1 >= -1:
#                         return "FORWARD-" + str(throttle(AXIS_1))
#                     else:
#                         return "BACKWARD-" + str(throttle(AXIS_1))
#                 elif event.__dict__.get("axis") == 0:
#                     if AXIS_0 < 0 and AXIS_0 >= -1:
#                         return "LEFT-" + str(throttle(AXIS_0))
#                     else:
#                         return "RIGHT-" + str(throttle(AXIS_0))
#                 elif round(AXIS_4) == -1 and round(AXIS_5) == -1:
#                     return "STOP-0"
#                 elif event.__dict__.get("axis") == 4:
#                     return "ROTATE_LEFT-" + str(throttle(AXIS_4))
#                 elif event.__dict__.get("axis") == 5:
#                     return "ROTATE_RIGHT-" + str(throttle(AXIS_5))
#                 else:
#                     return "STOP-"+"0"
#             return 0


def MOVE_Bot_1():
    Value = Controller_Elephant()
    if Value != 0:
        print(Value)
        client.publish("CONTROLLER_INPUTS_ELEPHANT", Value)

# def MOVE_Bot_2():
#     Value = Controller_Rabbit()
#     if Value != 0:
#         print(Value)
#         client.publish("CONTROLLER_INPUTS_RABBIT", Value)


client_id = "Controller"
port = 1883
broker = "192.168.140.134"  # or IP address

client = mqtt.Client(client_id)
if client.connect(broker, port) != 0:
    print("Could not connect to client")
    sys.exit(-1)

while True:
    MOVE_Bot_1()
    # MOVE_Bot_2()
