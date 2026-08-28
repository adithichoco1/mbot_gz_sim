import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String
import json
import os

class lidar1(Node):
    def __init__(self):
        super().__init__("lidar_1")

        self.lid_sub = self.create_subscription(
        LaserScan, "/scan", self.callback, 10
    )

        self.obs_pub = self.create_publisher(String, "obstacle", 10)

    def callback(self, msg):

        range = list(msg.ranges)
        range_min = msg.range_min 
        range_max = msg.range_max 
            
        safe_dist = 0.4 
        cleaned = [r if r > msg.range_min and r < msg.range_max else 10 for r in range]
        front = cleaned[350:360] + cleaned[0:10]
        front_left = cleaned[20:50]
        left = cleaned[70:110]
        right = cleaned[250:290]
        front_right = cleaned[310:340]

        dir = {
        "front_min" : min(front),
        "front_left_min" : min(front_left),
        "left_min" : min(left),
        "right_min" : min(right),
        'front_right_min' : min(front_right)
        }

        msgs = String()
        msgs.data = json.dumps(dir)
        self.obs_pub.publish(msgs)

def main():
    rclpy.init(args=None)
    lidarr = lidar1()
    rclpy.spin(lidarr)
    lidarr.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()