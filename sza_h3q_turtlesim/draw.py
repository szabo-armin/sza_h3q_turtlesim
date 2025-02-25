import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class SquareDrawer(Node):

    def __init__(self):
        super().__init__('square_drawer')
        self.cmd_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.draw_square()

    def draw_square(self):
        cmd_msg = Twist()
        side_length = 2.0  # Idő egy oldal rajzolására (másodperc)
        turn_time = 1.0    # Idő a forduláshoz
        linear_speed = 2.0 # Sebesség előrehaladáskor
        angular_speed = 1.57  # kb. 90 fok/sec (pi/2 radián)

        for _ in range(4):  # 4 oldal -> 4 mozgás + 4 fordulás
            # Egyenes vonal rajzolása
            cmd_msg.linear.x = linear_speed
            cmd_msg.angular.z = 0.0
            self.cmd_pub.publish(cmd_msg)
            time.sleep(side_length)

            # Fordulás (90 fok)
            cmd_msg.linear.x = 0.0
            cmd_msg.angular.z = angular_speed
            self.cmd_pub.publish(cmd_msg)
            time.sleep(turn_time)

        # Állítsuk meg a teknőst a végén
        cmd_msg.linear.x = 0.0
        cmd_msg.angular.z = 0.0
        self.cmd_pub.publish(cmd_msg)
        self.get_logger().info("Kocka rajzolása kész!")

def main(args=None):
    rclpy.init(args=args)
    square_drawer = SquareDrawer()
    rclpy.spin_once(square_drawer, timeout_sec=1)  # Csak egyszer fusson le
    square_drawer.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

