#! /usr/bin/env python
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import QuaternionStamped, Vector3Stamped, TransformStamped
from visualization_msgs.msg import Marker
from tf2_ros import TransformBroadcaster

import numpy as np
from scipy.spatial.transform import Rotation as R

class TiltVisualizer(Node):
    def __init__(self):
        super().__init__('tilt_visualizer')
        self.get_logger().info('Tilt visualizer node started...')

        self.quaternion_subscriber = self.create_subscription(QuaternionStamped, '/rotation', self.quaternion_callback, 10)
        self.rollpitch_subscriber = self.create_subscription(Vector3Stamped, '/tilt_angles', self.rollpitch_callback , 10)
        self.marker_publisher = self.create_publisher(Marker, '/imu_marker', 10)

        self.transform_broadcaster = TransformBroadcaster(self)
        self.transform_msg = TransformStamped()
        self.transform_msg.header.frame_id = 'global'
        self.transform_msg.child_frame_id = 'imu'
        self.transform_msg.transform.translation.z = 1.0 #raise slightly in rviz

        self.marker_msg = Marker()
        self.marker_msg.header.frame_id = 'imu'
        self.marker_msg.type = Marker.MESH_RESOURCE
        self.marker_msg.action = Marker.ADD
        self.marker_msg.mesh_resource = 'package://imu_lsm6dstrc_ros/mesh/adafruit_imu.stl'
        self.marker_msg.mesh_use_embedded_materials = True
        self.marker_msg.scale.x = 0.02
        self.marker_msg.scale.y = 0.02
        self.marker_msg.scale.z = 0.02
        self.marker_msg.color.r = 0.8
        self.marker_msg.color.g = 0.8
        self.marker_msg.color.b = 0.9
        self.marker_msg.color.a = 0.9
        self.marker_msg.pose.orientation.w = 1.0


    def quaternion_callback(self, msg):
        now = self.get_clock().now()
        self.transform_msg.header.stamp = now.to_msg() #use current time for the transform timestamp, not the IMU timestamp
        self.transform_msg.transform.rotation = msg.quaternion
        self.transform_broadcaster.sendTransform(self.transform_msg)
        
        self.marker_msg.header.stamp = now.to_msg()
        self.marker_publisher.publish(self.marker_msg)

    def rollpitch_callback(self, msg):
        roll = msg.vector.x
        pitch = msg.vector.y
        self.get_logger().info('roll(x): {roll:6.02f} deg,   pitch(y): {pitch:6.02f} deg'.format(roll=roll, pitch=pitch), throttle_duration_sec=0.1) #throttle_duration_sec limits how often the message is printed to the console (1 message per second in this case)'


def main(args=None):
    rclpy.init(args=args)
    tilt_visualizer = TiltVisualizer()
    rclpy.spin(tilt_visualizer)
    tilt_visualizer.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()