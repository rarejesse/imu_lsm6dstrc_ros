cmake_minimum_required(VERSION 3.8)
project(imu_lsm6dstrc_ros)

find_package(ament_cmake REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)

ament_python_install_package(${PROJECT_NAME})

install(PROGRAMS
  scripts/imu_settings_test.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/imu_publisher.py
  DESTINATION lib/${PROJECT_NAME}
)

# install(PROGRAMS
#   scripts/tilt_calculator.py
#   DESTINATION lib/${PROJECT_NAME}
# )

install(PROGRAMS
  scripts/tilt_visualizer.py
  DESTINATION lib/${PROJECT_NAME}
)

install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

install(
  DIRECTORY config
  DESTINATION share/${PROJECT_NAME}
)

install(
  DIRECTORY mesh
  DESTINATION share/${PROJECT_NAME}
)


ament_package()
