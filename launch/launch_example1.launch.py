from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            # Node(
            #     package='foxglove_bridge',
            #     executable='foxglove_bridge',
            #     parameters=[
            #         {'port': 8765},
            #         {'address': '0.0.0.0'},
            #         {'tls': False},
            #         {'certfile': ''},
            #         {'keyfile': ''},
            #         # {'topic_whitelist': "'.*'"},
            #         {'max_qos_depth': 10},
            #         {'num_threads': 0},
            #         {'use_sim_time': False},
            #     ]
            # ),
            Node(
                package='sza_h3q_turtlesim',
                executable='draw',
                output='screen'
            ),
            Node(
                package='turtlesim',
                executable='turtlesim_node',
            ),
        ]
    )


# from launch import LaunchDescription
# from launch_ros.actions import Node

# def generate_launch_description():
#     return LaunchDescription([
#         Node(
#             package='turtlesim',
#             # namespace='turtle1',
#             executable='turtlesim_node',
#             name='sim'
#         ),
#         Node(
#             package='sza_h3q_turtlesim',
#             executable='draw',
#             output='screen',
#         ),
#     ])