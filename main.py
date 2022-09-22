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

# Specifying that the below pins are Output Pins
# Motor 1 Pins
GPIO.setup(ENA_PIN, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

# Motor 2 Pins
GPIO.setup(ENB_PIN, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Ultrasonic Sensor Pins
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

# robot.stop()

#x = Sensor.ultrasonic()
# print(x)


def main():
    robot.forward(1)
    time.sleep(1)
    robot.backward(1)
    time.sleep(1)

    GPIO.cleanup()


main()
