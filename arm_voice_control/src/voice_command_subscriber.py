#!/usr/bin/env python
import rospy
import os
import rospy
import rospkg
import subprocess
import roslaunch
from std_srvs.srv import Trigger, TriggerResponse

from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Voice command received:  %s", data.data)
    if data.data >="Plan1":
        start_node_direct('reach_up_pose_execute.py')
        # wait for the previous movement to end
        rospy.sleep(12)
        start_node_direct('place_on_table_execute.py')
        # wait for the previous movement to end
        rospy.sleep(22)
        start_node_direct('release_bottle_on_table_execute.py')


############## FROM:
# https://answers.ros.org/question/42849/how-to-launch-a-launch-file-from-python-code/
# Start:---------------------------------------------------------------------------------------------
    # package = 'mover4_moveit_config'
    # executable = 'mover4_named_position_replay.py'
    # node_name = 'mover4_move_group_python_interface'

def start_node_direct(nn):
    """
    Does work as well from service/topic callbacks directly using rosrun
    """    
    package = 'mover4_moveit_config'
    # node_name = 'mover4_named_position_replay.py'
    node_name = nn

    command = "rosrun {0} {1}".format(package, node_name)

    p = subprocess.Popen(command, shell=True)

    state = p.poll()
    if state is None:
        rospy.loginfo("process is running fine")
    elif state < 0:
        rospy.loginfo("Process terminated with error")
    elif state > 0:
        rospy.loginfo("Process terminated without error")


# def start_node2():
#     """
#     Does work as well from service/topic callbacks using launch files
#     """    
#     package = 'YOUR_PACKAGE'
#     launch_file = 'YOUR_LAUNCHFILE.launch'

#     command = "roslaunch  {0} {1}".format(package, launch_file)

#     p = subprocess.Popen(command, shell=True)

#     state = p.poll()
#     if state is None:
#         rospy.loginfo("process is running fine")
#     elif state < 0:
#         rospy.loginfo("Process terminated with error")
#     elif state > 0:
#         rospy.loginfo("Process terminated without error")

# End---------------------------------------------------------------------------------------------------
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('arm_voice_command_listener', anonymous=True)

    rospy.Subscriber("arm_voice_control/voice_command", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()