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

# =================================================== #
# =================== Ultrasonic Sensor PINS ===================== #
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

# =================================================== #
# =================== IR Sensor PIN ===================== #
GPIO.setup(IR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def main():
    #    robot.forward(5)
 #   time.sleep(0.5)
    #    robot.forward(50, 99)
    #    time.sleep(0.5)
    #    robot.forward(10, 85)
    #    time.sleep(0.5)
    #    robot.forward(10, 70)
    #    time.sleep(0.5)
    robot.forward(10, 55)
    time.sleep(0.5)
#    robot.forward(10, 40)
#    time.sleep(0.5)
#    robot.forward(10, 25)
#    time.sleep(0.5)
#    robot.forward(10, 10)

    try:
        while True:
            right = sensor.ultrasonic(TRIG_PIN_A, ECHO_PIN_A)
            left = sensor.ultrasonic(TRIG_PIN_B, ECHO_PIN_B)
            x = sensor.ir()
            print(right, left, x)

    except (KeyboardInterrupt, TypeError):
        GPIO.cleanup()
        print(" Cleanup successful")


    # robot.calF()
    # robot.calB()
    # robot.calR()
    # robot.calL()
main()
