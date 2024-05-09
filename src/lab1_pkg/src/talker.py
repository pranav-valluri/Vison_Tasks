#!/usr/bin/env python3

import rospy as rp
from ackermann_msgs.msg import AckermannDriveStamped as ads



def talker():
    pub=rp.Publisher('drive',ads,queue_size=1)

    rp.init_node('talker', anonymous=True)
    rate= rp.Rate(1)
    while not rp.is_shutdown():
        v= rp.get_param('~v',0.0)
        d= rp.get_param('~d',0.0)
        drive_msg = ads()

        drive_msg.drive.speed = v

        drive_msg.drive.steering_angle = d
        msg="velocity:"+f"{v}"+"steering_angle:"+f"{d}"
        rp.loginfo(msg)

        pub.publish(drive_msg)
        
        

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rp.ROSInterruptException:
        pass


    