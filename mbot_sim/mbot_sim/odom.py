import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry 

class odom(Node):
    def __init__(self):
        super().__init__('Odometry')

        self.odo = self.create_subscription(Odometry, 'odom', self.odom_callback, 10)

    def odom_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.x
        self.get_logger().info(f"x = {x}, y = {y}")

def main():
    rclpy.init(args = None)
    odom1 = odom()
    rclpy.spin(odom1)
    odom1.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
           