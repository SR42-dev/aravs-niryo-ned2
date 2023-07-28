#!/usr/bin/env python

# this node takes an input stream from the arm camera feed and displays it

import sys
import cv2
import rospy
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge, CvBridgeError
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

bridge = CvBridge()

def imageCallback(ros_image):

    global bridge

    try:
        img = bridge.compressed_imgmsg_to_cv2(ros_image, "bgr8")
    except CvBridgeError as e:
            print(e)

    ##############################################################
    # from this point on, 'img' is the target of processing
    ##############################################################
    cv2.imshow("Image", img)
    ##############################################################

    cv2.waitKey(1)

  
def main(args):

    global out

    rospy.init_node('armcam', anonymous=True)

    imageTopic = "/niryo_robot_vision/compressed_video_stream"
    image_sub = rospy.Subscriber(imageTopic,CompressedImage, imageCallback)

    print("Press ctrl + c to trigger a KeyboardInterrupt.")

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down.")

    cv2.destroyAllWindows()
    print("Shutdown complete.")

if __name__ == '__main__':

    main(sys.argv)