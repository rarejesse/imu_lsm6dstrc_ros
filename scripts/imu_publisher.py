#!/usr/bin/env python3

import board
from adafruit_lsm6ds import Rate
from adafruit_lsm6ds.lsm6ds3trc import LSM6DS3TRC

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion

class ImuPublisher(Node):
    def __init__(self):
        super().__init__('imu_publisher')
        self.imu_publisher = self.create_publisher(Imu, 'imu', 10)
        publish_rate = 100 
        self.timer = self.create_timer(1.0/publish_rate, self.timer_callback)

        # Initialize sensor
        self.i2c = board.I2C()
        self.sensor = LSM6DS3TRC(self.i2c)
        self.get_logger().info('LSM6DS3TRC IMU initialized.')

        # Initialize IMU message and static fields
        self.msg = Imu()
        self.msg.header.frame_id = 'imu'

    def timer_callback(self):
        self.msg.header.stamp = self.get_clock().now().to_msg()
        self.msg.linear_acceleration.x, self.msg.linear_acceleration.y, self.msg.linear_acceleration.z = self.sensor.acceleration
        self.msg.angular_velocity.x, self.msg.angular_velocity.y, self.msg.angular_velocity.z = self.sensor.gyro
        self.imu_publisher.publish(self.msg)

def main():
    rclpy.init()
    imu_publisher = ImuPublisher()
    try:
        rclpy.spin(imu_publisher)
    except KeyboardInterrupt:
        imu_publisher.get_logger().info('Shutting down IMU publisher node')
    imu_publisher.destroy_node()
    rclpy.shutdown()

    

if __name__ == '__main__':
    main()