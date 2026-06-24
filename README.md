# ROS2 Driver for Adafruit lsm6dstrc IMU

After building this ROS2 package, run the following command on the Raspberry Pi:

```
ros2 run imu_lsm6dstrc_ros imu_pblisher.py
```

To run the visualizer Rviz script (on your computer/docker environment, not on the Raspberry Pi) run:

```
ros2 launch imu_lsm6dstrc_ros tilt_visualizer.launch.py
```
