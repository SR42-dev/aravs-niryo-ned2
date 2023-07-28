#!/usr/bin/env python

# an implementation of armcam.py using the ROS wrapper

from niryo_robot_python_ros_wrapper import *
import rospy
import cv2

# Initializing ROS node
rospy.init_node('niryo_ned_example_python_ros_wrapper')

niryo_robot = NiryoRosWrapper()

while True:
    
    img=niryo_robot.get_compressed_image()

    cv2.imshow('feed', img)

    if cv2.waitKey(0) & 0xff == ord('q'):
        break

# - Constants
workspace_name = "workspace_1" # Robot's Workspace Name

# The observation pose
observation_pose = (0.18, 0., 0.35, 0., 1.57, -0.2)
# The Place pose
place_pose = (0., -0.25, 0.1, 0., 1.57, -1.57)

# - Main Program
# Calibrate robot if robot needs calibration
niryo_robot.calibrate_auto()
# Changing tool
#niryo_robot.update_tool()