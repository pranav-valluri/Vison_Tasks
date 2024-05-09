#!/usr/bin/env python3

import os
import rospy
import roslaunch

def launch_nodes():
    rospy.init_node('lab1_launch', anonymous=True)

    rospy.set_param('~v', 2.0)
    rospy.set_param('~d', 1.0)

    package_name = 'lab1_pkg'
    talker_path = os.path.join(os.path.dirname(__file__), 'talker.py')
    relay_path = os.path.join(os.path.dirname(__file__), 'relay.py')

    talker_node = roslaunch.core.Node(package_name, 'talker.py', name='talker')
    talker_launch = roslaunch.scriptapi.ROSLaunch()
    talker_launch.start()
    talker_process = talker_launch.launch(talker_node)

    relay_node = roslaunch.core.Node(package_name, 'relay.py', name='relay')
    relay_launch = roslaunch.scriptapi.ROSLaunch()
    relay_launch.start()
    relay_process = relay_launch.launch(relay_node)

    rospy.spin()

if __name__ == '__main__':
    try:
        launch_nodes()
    except rospy.ROSInterruptException:
        pass
