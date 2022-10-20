import time
import RPi.GPIO as GPIO
from definitions import *
# GPIO.setmode(GPIO.BOARD)

# Robot class with functions that allow Robot to move forward, backward, left and right


class Robot:
    def __init__(self):
        self.myPWM = GPIO.PWM(ENA_PIN, 100)
        self.myPWM2 = GPIO.PWM(ENB_PIN, 100)
        self.myPWM.start(0)
        self.myPWM2.start(0)

    # Both motors are rotating forward
    # distance in meter
    def forward(self, pwm_left, pwm_right):
        # Motor # 1
        # Creating a PWM object
        #myPWM = GPIO.PWM(ENA_PIN, 100)
        if pwm_left > 0:
            self.myPWM.ChangeDutyCycle(pwm_left)

            GPIO.output(IN1, GPIO.HIGH)
            GPIO.output(IN2, GPIO.LOW)
        elif pwm_left < 0:

            self.myPWM.ChangeDutyCycle(abs(pwm_left))
            GPIO.output(IN1, GPIO.LOW)
            GPIO.output(IN2, GPIO.HIGH)

        # Motor # 2
        # myPWM2 = GPIO.PWM(ENB_PIN, 100)
        if pwm_right > 0:
            self.myPWM2.ChangeDutyCycle(pwm_right)

            GPIO.output(IN3, GPIO.LOW)
            GPIO.output(IN4, GPIO.HIGH)
        elif pwm_right < 0:
            self.myPWM2.ChangeDutyCycle(abs(pwm_right))
            GPIO.output(IN3, GPIO.HIGH)
            GPIO.output(IN4, GPIO.LOW)
        # velocity = 3.1555e-3*(pwm) + 0.0267

        # # Time
        # t = distance/velocity
        # # Time measurement is in seconds

    # # Both motors are rotating backward

    # def backward(self, pwm):
    #     #myPWM = GPIO.PWM(ENA_PIN, 100)
    #     self.myPWM.ChangeDutyCycle(pwm)

    #     GPIO.output(IN2, GPIO.HIGH)
    #     GPIO.output(IN1, GPIO.LOW)
    # #  myPWM.ChangeDutyCycle(99)
    #     #myPWM2 = GPIO.PWM(ENB_PIN, 100)
    #     self.myPWM2.ChangeDutyCycle(pwm)

    #     GPIO.output(IN4, GPIO.LOW)
    #     GPIO.output(IN3, GPIO.HIGH)

    # Right motor runs backward while left motor runs forward

    def left(self, degree, pwm=20):

        #myPWM = GPIO.PWM(ENA_PIN, 100)
        self.myPWM.ChangeDutyCycle(pwm)

        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN1, GPIO.LOW)

        #myPWM2 = GPIO.PWM(ENB_PIN, 100)
        self.myPWM2.ChangeDutyCycle(pwm)

        # t = (degree + 20.333)/209.71

        GPIO.output(IN4, GPIO.HIGH)
        GPIO.output(IN3, GPIO.LOW)
        #t = (10 + 4)/183.71
        t = (degree + 4)/183.71
        time.sleep(t)

    # Right motor runs forward while left motor runs backward

    def right(self, degree, pwm=20):
        # delay because we want the robot still before it turns

        self.myPWM.ChangeDutyCycle(pwm)

        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN1, GPIO.HIGH)

        #myPWM2 = GPIO.PWM(ENB_PIN, 100)
        self.myPWM2.ChangeDutyCycle(pwm)

        GPIO.output(IN4, GPIO.LOW)
        GPIO.output(IN3, GPIO.HIGH)

        t = (degree + 4)/183.71
        time.sleep(t)

    def stop(self):
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        self.myPWM.ChangeDutyCycle(0)
        self.myPWM2.ChangeDutyCycle(0)

# ============================================ #
# ============= Hard coded =================== #

    # Both motors are rotating forward
    # distance in meter
    def calF(self, distance, pwm):
        # Motor # 1
        # Creating a PWM object
        #myPWM = GPIO.PWM(ENA_PIN, 100)
        self.myPWM.ChangeDutyCycle(pwm)

        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)

        # Motor # 2
        #myPWM2 = GPIO.PWM(ENB_PIN, 100)
        self.myPWM2.ChangeDutyCycle(pwm)
    #    myPWM.ChangeFrequency(1000)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)
        # The Pwm specified won't matter when we have the formula below
        velocity = 3.1555e-3*(pwm) + 0.0267

        # Time
        t = distance/velocity
        # Time measurement is in seconds
        time.sleep(t)

    # Both motors are rotating backward

    def calB(self, distance, pwm):
        #myPWM = GPIO.PWM(ENA_PIN, 100)
        self.myPWM.ChangeDutyCycle(pwm)

        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN1, GPIO.LOW)
    #  myPWM.ChangeDutyCycle(99)
        #myPWM2 = GPIO.PWM(ENB_PIN, 100)
        self.myPWM2.ChangeDutyCycle(pwm)

        GPIO.output(IN4, GPIO.LOW)
        GPIO.output(IN3, GPIO.HIGH)

        time.sleep(distance*1)

    # Right motor runs backward while left motor runs forward

    def calL(self, degree, pwm):
        # time.sleep(0.1)
        #myPWM = GPIO.PWM(ENA_PIN, 100)
        self.myPWM.ChangeDutyCycle(pwm)

        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN1, GPIO.LOW)

        #myPWM2 = GPIO.PWM(ENB_PIN, 100)
        self.myPWM2.ChangeDutyCycle(pwm)

        t = (degree + 4)/183.71

        GPIO.output(IN4, GPIO.HIGH)
        GPIO.output(IN3, GPIO.LOW)

        time.sleep(t)

    # Right motor runs forward while left motor runs backward

    def calR(self, degree, pwm):
        # delay because we want the robot still before it turns

        #myPWM = GPIO.PWM(ENA_PIN, 100)
        self.myPWM.ChangeDutyCycle(pwm)

        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN1, GPIO.HIGH)

        #myPWM2 = GPIO.PWM(ENB_PIN, 100)
        self.myPWM2.ChangeDutyCycle(pwm)

        GPIO.output(IN4, GPIO.LOW)
        GPIO.output(IN3, GPIO.HIGH)

        t = (degree + 4)/183.71
        time.sleep(t)

    def changeCycle(self):
        self.myPWM.ChangeDutyCycle(pwm)
        self.myPWM2.ChangeDutyCycle(pwm)

    def stop(self):
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
