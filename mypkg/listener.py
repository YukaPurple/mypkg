# SPDX-FileCopyrightText: 2023 Yukari Watarai
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from person_msgs.msg import Person

def cb(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data) 

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Person, "countup", cb, 10) 

rclpy.spin(node)
