#!/usr/bin/env python

from __future__ import print_function
from __future__ import division

import roslib
roslib.load_manifest('turtlebot3_gpio_control')

import sys
import rospy
# import cv2
# import imutils

# from std_msgs.msg import String
from std_msgs.msg import Bool
# from sensor_msgs.msg import Image
# from sensor_msgs.msg import RegionOfInterest
# from sensor_msgs.msg import CameraInfo
#
# from cv_bridge import CvBridge
# from cv_bridge import CvBridgeError

import numpy as np

import RPi.GPIO as GPIO
import time


class blink_led_node:
    def __init__(self):
        """ init RPi GPIO """
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(12, GPIO.OUT)

        """  Initializing your ROS Node """
        rospy.init_node('blink_led_node', anonymous=True)

        rospy.on_shutdown(self.shutdown)

        """ Subscribe to the Bool topic """
        self.imgRaw_sub = rospy.Subscriber("/led_blink", Bool, self.callback)

    def callback(self,data):
        if (data.data == True):
            rospy.loginfo("LED ON!")
            GPIO.output(12, GPIO.HIGH)

        elif (data.data == False):
            rospy.logerr("LED OFF!")
            GPIO.output(12, GPIO.LOW)

    def shutdown(self):
        try:
            rospy.loginfo("Blink LED node [OFFLINE]...")

        finally:
            GPIO.cleanup()

def usage():
    print("%s" % sys.argv[0],)

def main(args):
    vn = blink_led_node()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Blink LED node [OFFLINE]...")


if __name__ == '__main__':
    if len(sys.argv) < 1:
        print(usage())
        sys.exit(1)
    else:
        print("Blink LED node [ONLINE]...")
        main(sys.argv)
