import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math

class CubeDrawer(Node):
    def __init__(self):
        super().__init__('cube_drawer')
        self.cmd_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.draw_cube()

    def move(self, linear_x=0.0, angular_z=0.0, duration=1.0):
        cmd_msg = Twist()
        cmd_msg.linear.x = linear_x
        cmd_msg.angular.z = angular_z
        self.cmd_pub.publish(cmd_msg)
        time.sleep(duration)

    def draw_cube(self):
        side_length = 2.0
        depth_length = 1.5

        for _ in range(4):
            self.move(linear_x=side_length, duration=1.0)
            self.move(angular_z=math.pi / 2, duration=1.0)

        self.move(angular_z=-math.pi / 4, duration=1.0)
        self.move(linear_x=depth_length, duration=1.0)
        self.move(angular_z=math.pi / 4, duration=1.0)  

        for _ in range(4):
            self.move(linear_x=side_length, duration=1.0)
            self.move(angular_z=math.pi / 2, duration=1.0)

        self.move(angular_z=-math.pi / 4, duration=1.0)  
        self.move(linear_x=-depth_length, duration=1.0)  
        self.move(angular_z=math.pi / 4, duration=1.0)  
        self.move(linear_x=side_length, duration=1.0)  
        self.move(angular_z=-math.pi / 4, duration=1.0)  
        self.move(linear_x=depth_length, duration=1.0)  
        self.move(angular_z=math.pi / 4, duration=1.0)  
        self.move(angular_z=math.pi / 2, duration=1.0)  
        self.move(linear_x=side_length, duration=1.0)  
        self.move(angular_z=math.pi / 4, duration=1.0)  
        self.move(linear_x=depth_length, duration=1.0)  
        self.move(angular_z=math.pi / 4, duration=1.0)  
        self.move(linear_x=side_length, duration=1.0)  
        self.move(angular_z=3 * math.pi / 4, duration=1.0)  
        self.move(linear_x=depth_length, duration=1.0)  

        self.get_logger().info("3D kocka kész!")

        self.move(linear_x=0.0, angular_z=0.0)

def main(args=None):
    rclpy.init(args=args)
    cube_drawer = CubeDrawer()
    rclpy.spin_once(cube_drawer, timeout_sec=1)
    cube_drawer.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()