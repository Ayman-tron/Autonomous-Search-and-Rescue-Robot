import time
from move import *
import RPi.GPIO as GPIO
from definitions import *
from distance import *

# Creating a robot object
robot = Robot()

# Creating a sensor objuct
sensor = Sensor()

GPIO.setmode(GPIO.BOARD)

# =================================================== #
# =================== Motor Driver Pin ===================== #
# Specifying that the below pins are Output Pins
# Motor 1 Pins
GPIO.setup(ENA_PIN, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

# Motor 2 Pins
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
GPIO.setup(IR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def get_data():
    right = sensor.ultrasonic(TRIG_PIN_A, ECHO_PIN_A)
    left = sensor.ultrasonic(TRIG_PIN_B, ECHO_PIN_B)
    front = sensor.ultrasonic(TRIG_PIN_C, ECHO_PIN_C)
    x = sensor.ir()
    return (right, left, front, x)

# pwm signal for turning should be 40
# The argument for the turning functions are degrees and pwm
# The argument for the forward and backward is distance and pwm


def main():
    try:
        while True:
            distance = get_data()
            right = distance[0]
            left = distance[1]
            front = distance[2]
            ir = distance[3]

            '''if (2.00 < left < 7.00) and ir == 1:
                robot.forward(50)
            elif (ir == 0):
                robot.stop()
                robot.right(90, 35)'''

            print(right, left, front, ir)
    except (KeyboardInterrupt, TypeError):
        GPIO.cleanup()
        print(" Cleanup successful")

    # robot.calF()
    # robot.calB()
    # robot.calR()
    # robot.calL()
main()
