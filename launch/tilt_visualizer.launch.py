from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description(): 
    """
    All launch files need to have this function
    This function must return a LaunchDescription object
    You can add nodes to a LaunchDescription object using the add_action() method
    The DelareLaunchArgument variables define options you can use on the command line when you launch this file
    For example, to run the demo without rviz:
    """
    package_dir = get_package_share_directory('imu_lsm6dstrc_ros')
    print('THE PACKAGE DIR IS: ', package_dir)

    enable_rviz = DeclareLaunchArgument(name='enable_rviz',
                                        default_value='true',   
                                        description='start rviz with provided config file')

    # tilt_calculator_node = Node(executable='tilt_calculator.py',  
    #                  package='imu_lsm6dstrc_ros')
    
    tilt_visualizer_node = Node(executable='tilt_visualizer.py',  
                     package='imu_lsm6dstrc_ros')
    
    rviz_node = Node(executable='rviz2', 
                     condition=IfCondition(LaunchConfiguration('enable_rviz')),
                     package='rviz2', 
                     arguments=['-d', os.path.join(package_dir, 'config', 'tilt_visualizer.rviz')])
    
    ld = LaunchDescription()            
    ld.add_entity(enable_rviz)
    # ld.add_entity(tilt_calculator_node)
    ld.add_entity(tilt_visualizer_node)
    ld.add_entity(rviz_node)

    return ld