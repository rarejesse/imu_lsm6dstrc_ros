#!/usr/bin/env python3
"""
This script reads data from the LSM6DS3TRC IMU sensor and prints it to the console in a CSV format.
It can be run directly, independently of ROS2, to verify that the sensor is working and producing data.

usage:
    python imu_printer.py
"""

import time  
import board
from adafruit_lsm6ds import Rate
from adafruit_lsm6ds.lsm6ds3trc import LSM6DS3TRC

i2c = board.I2C()
sensor = LSM6DS3TRC(i2c)

print('#time (s), acc_X (m/s^2), acc_Y (m/s^2), acc_Z (m/s^2), angvel_X (rad/s), angvel_Y (rad/s), angvel_Z (rad/s)')

while True:
    timestamp = time.time() #epoch time in float seconds
    acc_x, acc_y, acc_z = sensor.acceleration
    angvel_x, angvel_y, angvel_z = sensor.gyro
    print(f'{timestamp:.9f}, {acc_x:.6f}, {acc_y:.6f}, {acc_z:.6f}, {angvel_x:.6f}, {angvel_y:.6f}, {angvel_z:.6f}')
    time.sleep(0.01) 