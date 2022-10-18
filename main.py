from gc import callbacks
import time
from move import *
import RPi.GPIO as GPIO
from definitions import *
from distance import *
from pid_test import *
import numpy as np

GPIO.setmode(GPIO.BOARD)

# =================================================== #
# =================== Motor Driver Pin ===================== #
# Specifying that the below pins are Output Pins
# Motor 1 Pins left
GPIO.setup(ENA_PIN, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

# Motor 2 Pins right
GPIO.setup(ENB_PIN, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# ================================================================ #
# =================== Ultrasonic Sensor PINS ===================== #
GPIO.setup(TRIG_PIN_A, GPIO.OUT)
GPIO.setup(ECHO_PIN_A, GPIO.IN)

GPIO.setup(TRIG_PIN_B, GPIO.OUT)
GPIO.setup(ECHO_PIN_B, GPIO.IN)

GPIO.setup(TRIG_PIN_C, GPIO.OUT)
GPIO.setup(ECHO_PIN_C, GPIO.IN)

# ================================================================ #
# =================== IR Sensor PIN ============================== #

GPIO.setup(IR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# ================================================================ #
robot = Robot()
sensor = Sensor()


def get_data():
    right = sensor.ultrasonic(TRIG_PIN_A, ECHO_PIN_A)
    left = sensor.ultrasonic(TRIG_PIN_B, ECHO_PIN_B)
    front = sensor.ultrasonic(TRIG_PIN_C, ECHO_PIN_C)
    x = sensor.ir()
    return (right, left, front, x)

# pwm signal for turning should be 40
# The argument for the turning functions are degrees and pwm
# The argument for the forward and backward is distance and pwm


def turn(channel):
    #GPIO.wait_for_edge(IR_PIN, GPIO.FALLING)
    print("Obstacle Detected")
    #robot.right(90, 35)
    # robot.stop()


def main():
    try:
        while True:
            distance = get_data()
            # right = distance[0]
            # left = distance[1]
            # front = distance[2]
            ir = distance[3]
            pid = PID(P=0.5, I=0.15, D=0.08)
            # left = sensor.ultrasonic(TRIG_PIN_B, ECHO_PIN_B)

            right = sensor.ultrasonic(TRIG_PIN_A, ECHO_PIN_A)
            print("Right: " + str(right))
            #ir = sensor.ir()

            pid.SetPoint = 6
            pid_control = pid.update(right)
            # print(type(pid_control))
            # print(pid_control)

            if 0 < right < 15:
                if abs(pid_control) > 10 and ir == 1:
                    pid_control = np.sign(pid_control)*50

                if pid_control > 0 and ir == 1:
                    robot.forward(20, 15+pid_control)
                    print("new:"+str(pid_control))
                    print("turing left")
                elif pid_control < 0 and ir == 1:
                    robot.forward(20+abs(pid_control), 15)
                    print("turing right")
                    print("new:"+str(pid_control))
                elif ir == 0:
                    robot.stop()
                    time.sleep(2)
                    robot.left()
                    time.sleep(0.00001)
            elif 15 < right:
                robot.forward(20, 15)
            print("===================================")

    except (KeyboardInterrupt, TypeError):
        GPIO.cleanup()
        print(" Cleanup successful")

    # robot.calF()
    # robot.calB()
    # robot.calR()
    # robot.calL()


main()
