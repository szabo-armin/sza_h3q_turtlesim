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
        side_length = 2.0  # Az alapnégyzet oldalhossza
        depth_length = 1.5  # A mélység (perspektíva miatt kisebb)

        #   Első négyzet kirajzolása
        for _ in range(4):
            self.move(linear_x=side_length, duration=1.0)
            self.move(angular_z=math.pi / 2, duration=1.0)  # 90 fokos fordulás

        #   Mozgás a hátsó négyzet kezdőpontjára
        self.move(angular_z=-math.pi / 4, duration=1.0)  # 45 fok balra
        self.move(linear_x=depth_length, duration=1.0)  # Mélységbe mozgás
        self.move(angular_z=math.pi / 4, duration=1.0)  # 45 fok jobbra

        #   Hátsó négyzet kirajzolása
        for _ in range(4):
            self.move(linear_x=side_length, duration=1.0)
            self.move(angular_z=math.pi / 2, duration=1.0)

        #   Többi csúcs összekötése

        self.move(angular_z=-math.pi / 4, duration=1.0)  # 45 fok balra
        self.move(linear_x=-depth_length, duration=1.0)  # Vissza az A négyzethez
        self.move(angular_z=math.pi / 4, duration=1.0)  # 45 fok jobbra
        self.move(linear_x=side_length, duration=1.0)  # A2-be mozgás
        self.move(angular_z=-math.pi / 4, duration=1.0)  # 45 fok balra
        self.move(linear_x=depth_length, duration=1.0)  # B2-be mozgás
        self.move(angular_z=math.pi / 4, duration=1.0)  # 45 fok jobbra
        
        self.move(angular_z=math.pi / 2, duration=1.0)  # 90 fokos fordulás
        self.move(linear_x=side_length, duration=1.0)  # Vissza az A négyzethez
        self.move(angular_z=math.pi / 4, duration=1.0)  # 45 fok jobbra
        self.move(linear_x=depth_length, duration=1.0)  # Vissza az A négyzethez
        self.move(angular_z=math.pi / 4, duration=1.0)  # 45 fok jobbra
        self.move(linear_x=side_length, duration=1.0)  # Vissza az A négyzethez
        self.move(angular_z=3 * math.pi / 4, duration=1.0)  # 135 fokos fordulás
        self.move(linear_x=depth_length, duration=1.0)  # Vissza az A négyzethez

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