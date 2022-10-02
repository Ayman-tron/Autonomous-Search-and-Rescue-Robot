from gpiozero import Robot, DistanceSensor
from signal import pause
sensor = DistanceSensor(16, 18, max_distance=1, threshold_distance=0.2)
#robot = Robot(left=(4, 14), right=(17, 18))

def hello():
    print("In range")
def bye():
    print("bye")

sensor.when_in_range = hello()
sensor.when_out_of_range = bye()
pause()
