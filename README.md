# aravs-niryo-ned2
An autonomous refueller with a static robotic arm using visual odometry.

## Setup
- Clone aravs-niryo-ned2 into catkin_ws/src as 
```
cd catkin_ws/src
git clone https://github.com/SR42-dev/aravs-niryo-ned2.git
``````
- Navigate to catkin_ws and build the workspace as 
```
cd .. && catkin_make
```

## To Run
1. For the Niryo Ned2 representation of the concept, open NiryoStudio, upload ```monolith.py``` onto the robot after connecting and run.
2. For the ARAVS native implementation of the concept on the robot's on-board computer, run 
```
roslaunch aravs_niryo_ned2 staticarm_real.launch
```
3. For the ARAVS simulation on Gazebo, run 
```
roslaunch aravs_niryo_ned2 staticarm_gazebo.launch
```

#### Note : The latter two cases only detect whycon markers from the robot's camera feed and publish their poses on the ```/whycon/markers``` topic.


