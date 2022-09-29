from mpu6050 import mpu6050
import time


def imu_data(mpu):

    gyro_data = mpu.get_gyro_data()

    return gyro_data

while True:
    mpu = mpu6050(0x68)
    test = imu_data(mpu)
    print("Gyro X : "+str(test['x']))
    print("Gyro Y : "+str(test['y']))
    print("Gyro Z : "+str(test['z']))
    print()
    print("-------------------------------")
    time.sleep(2.5)
