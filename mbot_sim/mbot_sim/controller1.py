import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import json
import os

class controller1(Node):
    def __init__(self):
        super().__init__("controller_1")

        self.cont_subs = self.create_subscription(String, "obstacle", self.cont_callback, 10)

        self.vel = self.create_publisher(Twist, "cmd_vel", 10)
    def cont_callback(self, msg):
        dir = json.loads(msg.data)
        self.front = dir["front_min"]
        self.front_left = dir["front_left_min"]
        self.left = dir["left_min"]
        self.right = dir["right_min"]
        self.front_right = dir["front_right_min"]
        self.safe_dist = 0.7

        self.obstacle_action()

    def obstacle_action(self):
            cmd = Twist()
    
            if self.front > 0.5:
                cmd.linear.x = 0.2
                cmd.angular.z = 0.0
            else:
                cmd.linear.x = 0.0
                cmd.angular.z = 0.5
    
            self.vel.publish(cmd)


           
def main():
    rclpy.init(args=None)
    control = controller1()
    rclpy.spin(control)
    control.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
           
             
