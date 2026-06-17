#!/usr/bin/env python3
import time
import sys
sys.path.insert(0, '/home/jesse/circuitpython/lib/python3.10/site-packages')
import inspect
import board
from adafruit_lsm6ds import Rate
from adafruit_lsm6ds import AccelRange, GyroRange
from adafruit_lsm6ds.lsm6ds3trc import LSM6DS3TRC
print(inspect.getfile(board))

i2c = board.I2C() 
sensor = LSM6DS3TRC(i2c)

while True:
    print('The LSM6DS3TRC supports the following data rates:')
    print('{} \n'.format(list(Rate.string.values())))
    print('The LSM6DS3TRC supports the following accelerometer ranges:')
    print('{} \n'.format(list(AccelRange.string.values())))
    print('The LSM6DS3TRC supports the following gyroscope ranges:')
    print('{} \n'.format(list(GyroRange.string.values())))

    print('Current accelerometer range: +/- {} G'.format(AccelRange.string[sensor.accelerometer_range]))
    print('Current gyroscope range: {} deg/s'.format(GyroRange.string[sensor.gyro_range]))
    print()


    sensor.accelerometer_data_rate = Rate.RATE_12_5_HZ
    sensor.gyro_data_rate = Rate.RATE_12_5_HZ
    print('==========Data rate set to 12.5 Hz==========')
    for i in range(30):
        ax, ay, az = sensor.acceleration
        gx, gy, gz = sensor.gyro
        print(f'({ax:.6f}, {ay:.6f}, {az:.6f}, {gx:.6f}, {gy:.6f}, {gz:.6f})')
    print()

    sensor.accelerometer_data_rate = Rate.RATE_52_HZ
    sensor.gyro_data_rate = Rate.RATE_52_HZ
    print('==========Data rate set to 52 Hz==========')
    for i in range(30):
        ax, ay, az = sensor.acceleration
        gx, gy, gz = sensor.gyro
        print(f'({ax:.6f}, {ay:.6f}, {az:.6f}, {gx:.6f}, {gy:.6f}, {gz:.6f})')
    print()

    sensor.accelerometer_data_rate = Rate.RATE_104_HZ
    sensor.gyro_data_rate = Rate.RATE_104_HZ
    print('==========Data rate set to 104 Hz==========')
    for i in range(30):
        ax, ay, az = sensor.acceleration
        gx, gy, gz = sensor.gyro
        print(f'({ax:.6f}, {ay:.6f}, {az:.6f}, {gx:.6f}, {gy:.6f}, {gz:.6f})')
    print()

    sensor.accelerometer_data_rate = Rate.RATE_208_HZ
    sensor.gyro_data_rate = Rate.RATE_208_HZ
    print('==========Data rate set to 208 Hz==========')
    for i in range(30):
        ax, ay, az = sensor.acceleration
        gx, gy, gz = sensor.gyro
        print(f'({ax:.6f}, {ay:.6f}, {az:.6f}, {gx:.6f}, {gy:.6f}, {gz:.6f})')
    print()

    sensor.accelerometer_data_rate = Rate.RATE_416_HZ
    sensor.gyro_data_rate = Rate.RATE_416_HZ
    print('==========Data rate set to 416 Hz==========')
    for i in range(30):
        ax, ay, az = sensor.acceleration
        gx, gy, gz = sensor.gyro
        print(f'({ax:.6f}, {ay:.6f}, {az:.6f}, {gx:.6f}, {gy:.6f}, {gz:.6f})')
    print()
    break


#RUN THIS AWK COMMAND
# ./rate_test.py | awk '{ if ($0 != prev) print "\033[1;31m" $0 "\033[0m"; else print $0; prev=$0 }' filename
