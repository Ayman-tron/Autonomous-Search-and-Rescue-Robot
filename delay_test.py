import RPi.GPIO as GPIO
import time
from move import *

GPIO.setmode(GPIO.BOARD)

# Motor #1, PWM Pin 29
ENA_PIN = 29
# Motor #2, PWM Pin 31
ENB_PIN = 31

# Pin 11 and 12 allow us to control the direction of the Motor 1
IN1 = 11
IN2 = 12

# Pin 13 and 15 allow us to control the direction of the Motor 1
IN3 = 13
IN4 = 15
IR_PIN = 21
GPIO.setup(IR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(ENA_PIN, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

# Motor 2 Pins right
GPIO.setup(ENB_PIN, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
robot = Robot()
def ir():
    readVal = GPIO.input(IR_PIN)
    time.sleep(0.1)
    return readVal



while True:
    x = ir()
    
    
    print(x)
    if x ==1:
        print("go")
        robot.forward(5,100)
    elif x == 0:
        robot.stop()
        print("stop")
    print("===================================")
