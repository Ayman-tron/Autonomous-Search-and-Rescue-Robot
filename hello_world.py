import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# Motor #1
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

# Motor #2
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

# Motor # 1
GPIO.output(12, GPIO.LOW)
GPIO.output(11, GPIO.HIGH)

# Motor # 2
GPIO.output(15, GPIO.HIGH)
GPIO.output(13, GPIO.LOW)

# Wait 2.5 seconds
time.sleep(10)


# Motor # 1
#GPIO.output(12, GPIO.HIGH)
#GPIO.output(11, GPIO.LOW)

# Motor # 2
#GPIO.output(15, GPIO.LOW)
#GPIO.output(13, GPIO.HIGH)

# Wait 2.5 seconds
#time.sleep(5)

# Reset all the GPIO pins by setting them to LOW
GPIO.cleanup()
#GPIO.output(11, GPIO.LOW)
#GPIO.output(12, GPIO.LOW)
#GPIO.output(13, GPIO.LOW)
#GPIO.output(15, GPIO.LOW)
