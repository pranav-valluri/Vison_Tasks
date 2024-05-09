#!/usr/bin/env python3

import rospy as rp
from ackermann_msgs.msg import AckermannDriveStamped as ads

def callback(data):

    speed = data.drive.speed
    steering_angle = data.drive.steering_angle


    speed *= 3
    steering_angle *= 3


    new_drive_msg = ads()
    new_drive_msg.drive.speed = speed
    new_drive_msg.drive.steering_angle = steering_angle

    pub.publish(new_drive_msg)

def relay():
    rp.init_node('relay', anonymous=True)

    rp.Subscriber('drive', ads, callback)

    rp.spin()

if __name__ == '__main__':
    pub = rp.Publisher('drive_relay', ads, queue_size=10)
    try:
        relay()
    except rp.ROSInterruptException:
        pass
