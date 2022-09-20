import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
# Motor #1
# PWM Pin 3
GPIO.setup(3, GPIO.OUT)
# Pin 11 and 12 allow us to control the direction of the Motor 1
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

# Motor #2
# PWM Pin 5
# Pin 13 and 15 allow us to control the direction of the Motor 1
GPIO.setup(5, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

GPIO.output(11, GPIO.LOW)
GPIO.output(12, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(15, GPIO.LOW)


def main():
    forward(1)
    time.sleep(1)
    backward(1)
    time.sleep(1)
#    right()
#    left()
    reset()

# Reset all the GPIO pins by setting them to LOW


def reset():
    # Cleaning up the GPIO pin for next user
    GPIO.cleanup()

# Both motors are rotating forward


def forward(distance):
    # Motor # 1
    # Creating a PWM object
    myPWM = GPIO.PWM(3, 100)
    myPWM.start(99)

    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.LOW)

    # Motor # 2
    myPWM2 = GPIO.PWM(5, 100)
    myPWM2.start(99)
#    myPWM.ChangeFrequency(1000)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(15, GPIO.HIGH)

    # Time measurement is in seconds
    time.sleep(distance*1)
    stop()

# Both motors are rotating backward


def backward(distance):
    myPWM = GPIO.PWM(3, 100)
    myPWM.start(60)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(11, GPIO.LOW)
  #  myPWM.ChangeDutyCycle(99)
    myPWM2 = GPIO.PWM(5, 100)
    myPWM2.start(60)

    GPIO.output(15, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)

    time.sleep(distance*1)
    stop()

# Right motor runs backward while left motor runs forward


def right(distance):
    myPWM = GPIO.PWM(3, 100)
    myPWM.start(20)

    GPIO.output(12, GPIO.HIGH)
    GPIO.output(11, GPIO.LOW)

    myPWM2 = GPIO.PWM(5, 100)
    myPWM2.start(20)

    GPIO.output(15, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)

    time.sleep(distance*1)
    stop()

# Right motor runs forward while left motor runs backward


def left(distance):
    myPWM = GPIO.PWM(3, 100)
    myPWM.start(10)

    GPIO.output(12, GPIO.LOW)
    GPIO.output(11, GPIO.HIGH)

    myPWM2 = GPIO.PWM(5, 100)
    myPWM2.start(10)

    GPIO.output(15, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)

    time.sleep(distance*1)
    stop()


def stop():
    myPWM = GPIO.PWM(3, 100)
    myPWM.start(10)

    GPIO.output(12, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)

    myPWM2 = GPIO.PWM(5, 100)
    myPWM2.start(10)

    GPIO.output(15, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)

    time.sleep(5)

# Below functions will be used to calibrate the distance the robot moves
# ====================================================================== #
# ====================================================================== #


def calF():
    myPWM = GPIO.PWM(3, 100)
    myPWM.start(100)

    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.LOW)

    myPWM2 = GPIO.PWM(5, 100)
    myPWM2.start(100)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(15, GPIO.HIGH)

    # Wait 5 seconds
    time.sleep(3)

# Both motors are rotating backward


def calB():
    myPWM = GPIO.PWM(3, 100)
    myPWM.start(100)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(11, GPIO.LOW)

    myPWM2 = GPIO.PWM(5, 100)
    myPWM2.start(100)

    GPIO.output(15, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)

    time.sleep(3)

# Right motor runs backward while left motor runs forward


def calR():
    myPWM = GPIO.PWM(3, 100)
    myPWM.start(100)

    GPIO.output(12, GPIO.HIGH)
    GPIO.output(11, GPIO.LOW)

    myPWM2 = GPIO.PWM(5, 100)
    myPWM2.start(100)

    GPIO.output(15, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)

    time.sleep(3)

# Right motor runs forward while left motor runs backward


def calL():
    myPWM = GPIO.PWM(3, 100)
    myPWM.start(100)

    GPIO.output(12, GPIO.LOW)
    GPIO.output(11, GPIO.HIGH)

    myPWM2 = GPIO.PWM(5, 100)
    myPWM2.start(100)

    GPIO.output(15, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)

    time.sleep(3)


main()
