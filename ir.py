import time
import RPi.GPIO as GPIO
from definitions import *

GPIO.setmode(GPIO.BOARD)

GPIO.setup(IR_PIN, GPIO.IN)
obstacle_detected = False


def obstacle():
    readVal = GPIO.input(IR_PIN)
    # No obstacle
    if readVal == 1:
        time.sleep(0.1)
        return readVal

    # The IR sensor has been configured to detect any obstacle less than or equal to 5cm
    elif readVal == 0:
        time.sleep(0.1)
        return readVal


# while True:
#    x = obstacle()
#    if x:
#        print("An obstacle is present")
#    else:
#        print("No obstacle")
