#!/usr/bin/env python

# monolith.py
# this program performs all the necessary actions monolithically to test the over-arching functionality of the niryo robot

import time
import rospy
from niryo_robot_python_ros_wrapper import *

# Initializing ROS node
rospy.init_node('niryo_ned2_python_ros_wrapper')

niryo_robot = NiryoRosWrapper()

# The observation pose
observation_pose1 = (0.179, -0.015, 0.308, 2.815, 1.346, 2.791)
observation_pose2 = (-0.041, -0.208, 0.316, -2.854, 1.274, 1.788)

# calibration
niryo_robot.calibrate_auto()

# vacuum pump init
niryo_robot.update_tool()
niryo_robot.push_air_vacuum_pump()

# move to observation pose
niryo_robot.move_pose(*observation_pose1) 

# scan for objects
numObj = 2
curObj = 0

def fuelPickup():

	
	niryo_robot.move_pose(*observation_pose1)
	niryo_robot.move_to_object("monolith_ws", height_offset=-0.005, shape=ObjectShape.CIRCLE, color='ANY')
	niryo_robot.pull_air_vacuum_pump()

def fuelDrop():

	niryo_robot.move_pose(*observation_pose2)
	niryo_robot.move_to_object("monolith_ws1", height_offset=-0.3, shape=ObjectShape.CIRCLE, color='RED')
	niryo_robot.push_air_vacuum_pump()
	

while True:
	
	fuelPickup()

	fuelDrop()