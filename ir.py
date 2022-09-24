import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(21, GPIO.IN)


while True:
    sensor = GPIO.input(21)
    # No obstacle
    if sensor == 1:
        print("Nothing")
        time.sleep(0.1)
    elif sensor == 0:
        print("Something")
