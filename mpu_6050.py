from mpu6050 import mpu6050
import time
mpu = mpu6050(0x68)

def imu_data():
    print("Temp : "+str(mpu.get_temp()))
    print()

    gyro_data = mpu.get_gyro_data()

    return gyro_data

while True:
    test = imu_data()
    print("Gyro X : "+str(test['x']))
    print("Gyro Y : "+str(test['y']))
    print("Gyro Z : "+str(test['z']))
    print()
    print("-------------------------------")
    time.sleep(5)
