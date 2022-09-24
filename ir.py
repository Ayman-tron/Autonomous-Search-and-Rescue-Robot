import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(21, GPIO.IN)
obstacle_detected = False

def obstacle():	
while True:
    sensor = GPIO.input(21)
    # No obstacle
    if sensor == 1:
       obstacle_detected = False
       return obstacle_detected
       time.sleep(0.1)

    # The IR sensor has been configured to detect any obstacle less than or equal to 5cm
    elif sensor == 0:
        obstacle_detected = True
        return obstacle_detected
        time.sleep(0.1)


if obstacle_detected:
	print("An obstacle is present")
else:
	print("No obstacle")
