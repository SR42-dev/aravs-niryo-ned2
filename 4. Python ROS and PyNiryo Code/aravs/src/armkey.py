#!/usr/bin/env python

# keyboard controller for the arm using joint trajectory messages

import os
import sys
import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def perform_trajectory(a, b, c, d, e):
    rospy.init_node('arm_trajectory_publisher')
    contoller_name='/niryo_robot_follow_joint_trajectory_controller/command'
    trajectory_publisher = rospy.Publisher(contoller_name,JointTrajectory, queue_size=10)
    argv = sys.argv[1:]                         
    arm_joints = ['joint1','joint2','joint3','joint4', 'joint5']
    goal_positions = [ float(a) , float(b) , float(c) ,float(d) ,float(e)]
 
    rospy.loginfo("Goal Position set.")
    rospy.sleep(1)


    trajectory_msg = JointTrajectory()
    trajectory_msg.joint_names = arm_joints
    trajectory_msg.points.append(JointTrajectoryPoint())
    trajectory_msg.points[0].positions = goal_positions
    trajectory_msg.points[0].velocities = [0.0 for i in arm_joints]
    trajectory_msg.points[0].accelerations = [0.0 for i in arm_joints]
    trajectory_msg.points[0].time_from_start = rospy.Duration(3)
    rospy.sleep(1)
    trajectory_publisher.publish(trajectory_msg)


if __name__ == '__main__':

    msg = """
    Reading from the keyboard  and Publishing to trajectory_msgs
    ---------------------------
    Moving around:
        q    w    e    r    t    -    to increment the joint arguments

        a    s    d    f    g    -    to decrement the joint arguments

    Press Ctrl-C to quit
    """

    print(msg)

    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    while True :

        print("Current joint positions: " + str(a) + " " + str(b) + " " + str(c) + " " + str(d) + " " + str(e))
        
        command = input()

        if command == 'q':
            a = a + 1
        elif command == 'a':
            a = a - 1
        elif command == 'w':
            b = b + 1
        elif command == 's':
            b = b - 1
        elif command == 'e':
            c = c + 1
        elif command == 'd':
            c = c - 1
        elif command == 'r':
            d = d + 1
        elif command == 'f':
            d = d - 1
        elif command == 't':
            e = e + 1
        elif command == 'g':
            e = e - 1
        elif command == 'quit':
            break
        else :
            continue

        perform_trajectory(a, b, c, d, e)


