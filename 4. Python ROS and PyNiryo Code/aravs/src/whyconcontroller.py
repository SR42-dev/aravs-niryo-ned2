#!/usr/bin/env python

# this node takes an input stream from the whycon marker feed and controls it accordingly

import sys
import cv2
import copy
import rospy
import numpy as np
from math import pi
import pandas as pd
import moveit_msgs.msg
import moveit_commander
import geometry_msgs.msg
from std_msgs.msg import String
from sensor_msgs.msg import Image
from whycon.msg import MarkerArray
from matplotlib import pyplot as plt
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge, CvBridgeError
from moveit_commander.conversions import pose_to_list
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint


def callback(msg): # only detects and acts on the first marker

    try:
        
        x = msg.markers[0].position.x       # target position x
        y = msg.markers[0].position.y       # target position y
        z = msg.markers[0].position.z       # target position z
        w = msg.markers[0].orientation.w    # target orientation quaternion w

        print(x, y, z, w)

    except:
            print('No markers detected')

  
def main(args):

    rospy.init_node('whycon_controller', anonymous=True)

    whycon_markers = "/whycon/markers"
    marker_sub = rospy.Subscriber(whycon_markers, MarkerArray, callback)

    print("Press ctrl + c to trigger a KeyboardInterrupt.")

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down.")

    cv2.destroyAllWindows()
    print("Shutdown complete.")

if __name__ == '__main__':

    main(sys.argv)