from definitions import *
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)


class Sensor:
    def ultrasonic(self):
        try:
            while True:
                GPIO.output(TRIG_PIN, 1)
                time.sleep(1E-6)
                GPIO.output(TRIG_PIN, 0)

                while GPIO.input(ECHO_PIN) == 0:
                    pass
                # Gives us the system time (starting the stopwatch)
                echoStartTime = time.time()
                while GPIO.input(ECHO_PIN) == 1:
                    pass
                # Stopping the stopwatch
                echoStopTime = time.time()
                pingTravelTime = echoStopTime - echoStartTime

                distance = 34300 * (pingTravelTime/2)

                # sensor requires a delay before sending and receiving the ping
                time.sleep(0.2)
                # Rounding to two decimal point
                #print(round(distance, 2), 'cm')
                return distance

        except KeyboardInterrupt():
            GPIO.cleanup()
            print("Cleanup successful")
    # The IR sensor has been configured to detect any obstacle less than or equal to 5cm
    # 0 means there is an obstacle, while 1 means no obstacle

    def ir(self):
        try:
            readVal = GPIO.input(IR_PIN)
            time.sleep(0.1)
            return readVal

        except KeyboardInterrupt():
            GPIO.cleanup()
            print("Cleanup successful")
