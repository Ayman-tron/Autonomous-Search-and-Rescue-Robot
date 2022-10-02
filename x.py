from definitions import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
pwm = 50
# =================================================== #
# =================== Motor Driver Pin ===================== #
# Specifying that the below pins are Output Pins
# Motor 1 Pins
GPIO.setup(ENA_PIN, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

# Motor 2 Pins
GPIO.setup(ENB_PIN, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

        # Motor # 1
        # Creating a PWM object
#myPWM = GPIO.PWM(ENA_PIN, 100)
#myPWM.start(pwm)
GPIO.output(IN1, GPIO.HIGH)
GPIO.output(IN2, GPIO.LOW)

        # Motor # 2
#myPWM2 = GPIO.PWM(ENB_PIN, 100)
#myPWM2.start(pwm)

GPIO.output(IN3, GPIO.LOW)
GPIO.output(IN4, GPIO.HIGH)

time.sleep(self)
GPIO.cleanup()
