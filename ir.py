import time
import RPi.GPIO as GPIO
from definitions import *

GPIO.setmode(GPIO.BOARD)
# In case IR Pin 21 is disconnected the internal resistor of the Pi will ensure that the value does not 
# fluctuate between 1 and 0. In this case we are using a pull up resistor which means when the wire is disconnected
# Pin 21 will read a 1
GPIO.setup(IR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# The IR sensor has been configured to detect any obstacle less than or equal to 5cm
def obstacle():
    readVal = GPIO.input(IR_PIN)
    time.sleep(0.1)
    return readVal

# 0 means there is an obstacle, while 1 means no obstacle
while True:
    x = obstacle()
    print(x)
GPIO.cleanup()
