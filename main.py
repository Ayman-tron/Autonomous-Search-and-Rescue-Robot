from gc import callbacks
import time
from move import *
import RPi.GPIO as GPIO
from definitions import *
from distance import *
from pid import *
import numpy as np

# Creating a robot object


# Creating a sensor objuct
sensor = Sensor()
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

# =================================================== #
# =================== Motor Driver Pin ===================== #
# Specifying that the below pins are Output Pins
# Motor 1 Pins left
GPIO.setup(ENA_PIN, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

# Motor 2 Pins right
GPIO.setup(ENB_PIN, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# ================================================================ #
# =================== Ultrasonic Sensor PINS ===================== #
GPIO.setup(TRIG_PIN_A, GPIO.OUT)
GPIO.setup(ECHO_PIN_A, GPIO.IN)

GPIO.setup(TRIG_PIN_B, GPIO.OUT)
GPIO.setup(ECHO_PIN_B, GPIO.IN)

GPIO.setup(TRIG_PIN_C, GPIO.OUT)
GPIO.setup(ECHO_PIN_C, GPIO.IN)

# ================================================================ #
# =================== IR Sensor PIN ============================== #

GPIO.setup(IR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# ================================================================ #
robot = Robot()


def get_data():
    right = sensor.ultrasonic(TRIG_PIN_A, ECHO_PIN_A)
    left = sensor.ultrasonic(TRIG_PIN_B, ECHO_PIN_B)
    #front = sensor.ultrasonic(TRIG_PIN_C, ECHO_PIN_C)
    x = sensor.ir()
    return (right, left, x)

# pwm signal for turning should be 40
# The argument for the turning functions are degrees and pwm
# The argument for the forward and backward is distance and pwm


def turn(channel):
    #GPIO.wait_for_edge(IR_PIN, GPIO.FALLING)
    print("Obstacle Detected")
    #robot.right(90, 35)
    # robot.stop()


def main():
  # robot.forward(1, 60)
    # GPIO.add_event_detect(IR_PIN, GPIO.FALLING, callback=turn, bouncetime=2500)
    # robot.stop()

    try:
        while True:
            distance = get_data()
            # right = distance[0]
            # left = distance[1]
            # front = distance[2]
            ir = distance[2]

            pid = PID(P=27, I=12.0, D=0.5)
            # left = sensor.ultrasonic(TRIG_PIN_B, ECHO_PIN_B)

            right = sensor.ultrasonic(TRIG_PIN_A, ECHO_PIN_A)

            print("Right: " + str(right))

            #ir = sensor.ir()

            # 设定期望值
            pid.SetPoint = 7
            # 获取PID的输出
            pid_control = pid.update(right)
            # PID输出限幅
            if pid_control > 100:
                pid_control = 100
            elif pid_control < -100:
                pid_control = -100
            # PID区间映射 0~8
            pid_control = pid_control * 0.08

            if pid_control > 0 and ir == 1:
                robot.forward(15, (15+pid_control))
                print("PWM" + "(15," + str(15+(pid_control))+")")
                print("turing left")
            elif pid_control < 0 and ir == 1:
                robot.forward(15+abs(pid_control), 15)
                print("PWM" + "(" + str(15+abs(pid_control))+",15)")
                print("turing right")

            if ir == 0:
                robot.stop()
                time.sleep(3)
                print("stop")
                robot.left(120, 20)
                robot.stop()
                print("I want to stop")
                time.sleep(10)

            print("===================================")

    except (KeyboardInterrupt, TypeError):
        GPIO.cleanup()
        print(" Cleanup successful")

    # robot.calF()
    # robot.calB()
    # robot.calR()
    # robot.calL()


main()
