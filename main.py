import time
from move import *
import RPi.GPIO as GPIO
from definitions import *
from distance import *
from main import *
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
    try:
        while True:
            x = sensor.ir()
            print(x)
    except KeyboardInterrupt():
        GPIO.cleanup()
        print("Cleanup successful")

    # robot.calF()
    # robot.calB()
    # robot.calR()
    # robot.calL()
main()
