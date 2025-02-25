import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class TriangleDrawer(Node):

    def __init__(self):
        super().__init__('triangle_drawer')
        self.cmd_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.draw_triangle()

    def draw_triangle(self):
        cmd_msg = Twist()
        side_length = 2.0
        turn_time = 1.0
        linear_speed = 2.0
        angular_speed = 1.57

        for _ in range(3):
            cmd_msg.linear.x = linear_speed
            cmd_msg.angular.z = 0.0
            self.cmd_pub.publish(cmd_msg)
            time.sleep(side_length)

            cmd_msg.linear.x = 0.0
            cmd_msg.angular.z = angular_speed
            self.cmd_pub.publish(cmd_msg)
            time.sleep(turn_time)

        cmd_msg.linear.x = 0.0
        cmd_msg.angular.z = 0.0
        self.cmd_pub.publish(cmd_msg)
        self.get_logger().info("Háromszög rajzolása kész!")

def main(args=None):
    rclpy.init(args=args)
    triangle_drawer = TriangleDrawer()
    rclpy.spin(triangle_drawer)  # Az eseményeket figyeli
    triangle_drawer.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
