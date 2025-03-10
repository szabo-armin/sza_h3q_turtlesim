from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package='sza_h3q_turtlesim',
                executable='draw',
                output='screen'
            ),
            Node(
                package='turtlesim',
                executable='turtlesim_node',
            ),
            Node(
            package='sza_h3q_turtlesim',
            executable='cube_publisher', 
            name='cube_publisher',
            output='screen',
        ),
        ]
    )
