from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            # namespace='turtle1',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='sza_h3q_turtlesim',
            executable='draw',
            output='screen',
        ),
    ])