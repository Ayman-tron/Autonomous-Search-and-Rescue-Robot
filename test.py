from gpiozero import DistanceSensor, LED
from signal import pause
from time import sleep
sensor = DistanceSensor(16, 18, max_distance=0.1, threshold_distance=0.07)
in_range = True

while True:
	if (sensor.when_in_range):
		print(True)
                sleep(1)
	else:
		print(False)
	        sleep(1)
