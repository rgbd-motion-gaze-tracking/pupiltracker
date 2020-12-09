# Pupil Tracker
The code take input from a RGB camera and detects face boundary and eyes boundaries. It detects the pupils within the eyes and gives their x- and y- coordinates and radii.
RBE526: Human Robot Interaction
Fall 2020
Code By: Aashirwad Patel
Date of Publishing: December 6, 2020

## Content:
This code was written as a part of individual coding assignment assigned to the students in the class. The code was solely developed by the author without external human aid and was used as a part of the project that used gaze data for interactive control of the robot, TRINA2.0, in ROS-Gazebo Simulation. The code is written in python 3.7 and developed under Windows 10 operating system using PyCharm IDE. 

## Required Packages: 
The code was developed with the all the latest packages of that time. Following are list of packages used and their corresponding versions.
1. opencv-python--version==4.4.0.46
2. matplotlib--version==3.3.3
3. numpy--version==1.19.3

Note: numpy--version==1.19.4 was the latest version back then though it had runtime errors in Windows 10 environment and the possible solution was to be released in the upcoming version (as per some articles online). 

## Execution:
1. Simply run the code by typing python3 EyeGazeTracker.py in terminal or run in any of the IDEs.
2. Provided the face is fully visible in the camera, the code successfully detects the face and the eyes.
3. Adjust the track bar to set the threshold value to enable pupil detection. The value usually is in between 30-100 depending upon the ambient light and illumination.

## Output:
1. Please check the documentation for the theory, pseudo code, and results.
2. Maximum comments are used in the script to make it easy for the reader to understand the code.
3. A short video demonstration is provided along with the submission. 

A short video presentation is found on: https://www.youtube.com/watch?v=QxNhjNDLaEM

Thank You!
